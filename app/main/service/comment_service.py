from app.main.model.gallery import Gallery
from app.main import db
from app.main.model.comment import Comment
from .auth_helper import Auth


def create_comment(request):

    resp = Auth.get_user_id_with_token(request)
    data = request.json

    new_comment = Comment(
        user_id=resp, gallery_id=data["gallery_id"], comment=data["comment"]
    )

    try:
        save_changes(new_comment)

    except Exception as e:
        response_object = {"status": "fail", "message": e}
        return response_object, 400

    response_object = {"status": "success", "message": "Successfully created."}
    return response_object, 201


def get_all_comments_on_this_gallery(request, id):
    return Comment.query.filter(Comment.gallery_id == id).all()


def delete_comment(request, id):
    resp = Auth.get_user_id_with_token(request)
    gallery = (
        Comment.query.filter(Comment.comment_id == id)
        .filter(Comment.user_id == resp)
        .first()
    )
    if gallery:
        db.session.delete(gallery)
        db.session.commit()
    else:
        response = {"status": "fail", "message": "This gallery does not exists"}
        return response, 404

    response = {"status": "success", "message": "Successfully delete gallery"}
    return response, 204


def save_changes(data):
    try:
        db.session.add(data)
        db.session.commit()
    except Exception as e:
        print(e)

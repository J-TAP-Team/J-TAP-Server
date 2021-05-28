from app.main import db
from app.main.model.gallery import *
from .auth_helper import Auth


def create_new_gallery(request):

    resp = Auth.get_user_id_with_token(request)
    data = request.json

    new_gallery = Gallery(
        user_id=resp, name=data["name"], description=data["description"]
    )

    try:
        save_changes(new_gallery)
    except Exception as e:
        response_object = {"status": "fail", "message": e}
        return response_object, 400

    response_object = {"status": "success", "message": "Successfully created."}
    return response_object, 201


def get_all_galleries(request):
    return Gallery.query.all()


def get_a_gallery(request, id):

    gallery = Gallery.query.filter(Gallery.gallery_id == id).first()

    sql = """
        SELECT p.picture_id, p.user_id, p.image, p.filename, p.description, p.created_at
        FROM picture p
        LEFT OUTER JOIN linkedgallerypicture l
        WHERE l.gallery_id = {}
    """

    pictures = db.session.execute(sql)
    print(pictures)

    gallery["pictures"] = pictures

    return gallery, 200


def delete_gallery(request, id):
    resp = Auth.get_user_id_with_token(request)
    gallery = (
        Gallery.query.filter(Gallery.gallery_id == id)
        .filter(Gallery.user_id == resp)
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

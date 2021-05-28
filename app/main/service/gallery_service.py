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


def get_my_gallery(request):

    resp = Auth.get_user_id_with_token(request)
    return Gallery.query.filter(user_id=resp).first()


def add_pictures(request):

    data = request.json

    try:
        gallery_id = data["gallery_id"]
        picture_list = data["pictures"]

        for id in picture_list:
            new_link = LinkedGalleryPicture(gallery_id=gallery_id, picture_id=id)

            save_changes(new_link)
    except Exception as e:
        response_object = {"status": "fail", "message": e}

        return response_object, 400

    response_object = {"status": "success", "message": "Successfully added."}
    return response_object, 201


def except_pictures(request):

    resp = Auth.get_user_id_with_token(request)
    data = request.json

    for i in data["pictures"]:

        link = (
            LinkedGalleryPicture.query.filter(
                LinkedGalleryPicture.gallery_id == data["gallery_id"]
            )
            .filter(LinkedGalleryPicture.picture_id == i)
            .filter(Gallery.user_id == resp)
            .first()
        )
        if link:
            db.session.delete(link)
            db.session.commit()
        else:
            continue

    response = {"status": "success", "message": "Successfully delete gallery"}
    return response, 204


def get_all_galleries(request):
    return Gallery.query.all()


def get_a_gallery(request, id):

    gallery = Gallery.query.filter(Gallery.gallery_id == id).first()

    if not gallery:
        response = {"status": "fail", "message": "This gallery does not exists"}
        return response, 404

    data = {
        "gallery_id": gallery.gallery_id,
        "user_id": gallery.user_id,
        "name": gallery.name,
        "description": gallery.description,
        "created_at": str(gallery.created_at),
    }

    row = (
        db.session.query(Picture)
        .join(
            LinkedGalleryPicture, Picture.picture_id == LinkedGalleryPicture.picture_id
        )
        .filter(LinkedGalleryPicture.gallery_id == id)
    ).all()

    pictures = []

    for r in row:
        obj = {
            "picture_id": r.picture_id,
            "image": r.image,
            "filename": r.filename,
            "description": r.description,
            "created_at": str(r.created_at),
        }
        pictures.append(obj)

    data["pictures"] = pictures

    count = db.session.query(Likes).filter(Likes.gallery_id == id).count()

    data["like"] = count

    return data, 200


def update_gallery(request, id):
    resp = Auth.get_user_id_with_token(request)
    gallery = (
        Gallery.query.filter(Gallery.gallery_id == id)
        .filter(Gallery.user_id == resp)
        .first()
    )
    if gallery:
        gallery.name = request.json["name"]
        gallery.description = request.json["description"]
        db.session.commit()
    else:
        response = {"status": "fail", "message": "This gallery does not exists"}
        return response, 404

    response = {
        "status": "success",
        "message": "Successfully updated gallery",
    }


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


def like_this_gallery(request):

    resp = Auth.get_user_id_with_token(request)
    data = request.json

    try:
        like = (
            Likes.query.filter(Likes.user_id == resp)
            .filter(Likes.gallery_id == data["gallery_id"])
            .first()
        )

        if like:
            db.session.delete(like)
            db.session.commit()

            response = {
                "status": "success",
                "message": "Successfully unlike this gallery",
            }
            return response, 204

        else:
            new_like = Likes(gallery_id=data["gallery_id"], user_id=resp)
            save_changes(new_like)

    except Exception as e:
        response = {"status": "fail", "message": e}
        return response, 404

    response = {"status": "success", "message": "Successfully like this gallery"}
    return response, 201


def save_changes(data):
    try:
        db.session.add(data)
        db.session.commit()
    except Exception as e:
        print(e)

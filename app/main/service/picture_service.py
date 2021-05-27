import datetime
import boto3
from werkzeug.utils import secure_filename

from app.main import db
from app.main.model.picture import Picture
from .auth_helper import Auth
from ..utils.util import Util


def upload_new_picture(request):

    resp = Auth.get_user_id_with_token(request)

    file = request.files["file"]
    filename = secure_filename(file.filename)

    url = Util.s3upload(file, filename)

    new_picture = Picture(user_id=resp, image=url, description=None)

    try:
        save_changes(new_picture)
    except Exception as e:
        response_object = {"status": "fail", "message": e}
        return response_object, 400

    response_object = {"status": "success", "message": "Successfully created."}
    return response_object, 201


def get_all_pictures(request):
    resp = Auth.get_user_id_with_token(request)
    return Picture.query.filter_by(user_id=resp).all()


def get_a_picture(request, id):

    picture = Picture.query.filter(Picture.picture_id == id).first()
    if picture.user_id != Auth.get_user_id_with_token(request):
        response = {
            "status": "fail",
            "message": "You don't have permission on this object",
        }
        return response, 403

    return picture, 200


def delete_picture(request, id):
    resp = Auth.get_user_id_with_token(request)
    picutre = (
        Picture.query.filter(Picture.picture_id == id)
        .filter(Picture.user_id == resp)
        .first()
    )
    if picutre:
        db.session.delete(picutre)
        db.session.commit()
    else:
        response = {"status": "fail", "message": "This picture does not exists"}
        return response, 404

    response = {"status": "success", "message": "Successfully delete picture"}
    return response, 204


def update_picture(request, id):
    resp = Auth.get_user_id_with_token(request)
    picture = (
        Picture.query.filter(Picture.picture_id == id)
        .filter(Picture.user_id == resp)
        .first()
    )
    if picture:
        picture.description = request.json["description"]
        db.session.commit()
    else:
        response = {"status": "fail", "message": "This picture does not exists"}
        return response, 404

    response = {
        "status": "success",
        "message": "Successfully updated picture description",
    }


def save_changes(data):
    try:
        db.session.add(data)
        db.session.commit()
    except Exception as e:
        print(e)

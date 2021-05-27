import datetime
import boto3
from werkzeug.utils import secure_filename

from app.main import db
from app.main.model.picture import Picture
from .auth_helper import Auth

from ..config import s3_config


def upload_new_picture(request):

    resp = Auth.get_user_id_with_token(request)
    # S3 업로드
    s3 = boto3.client(
        "s3",
        aws_access_key_id=s3_config["AccessKeyId"],
        aws_secret_access_key=s3_config["SecretKey"],
    )

    file = request.files["new_file"]
    filename = secure_filename(file.filename)
    bucket_name = s3_config["bucket_name"]
    s3.upload_file(file, bucket_name, filename)

    new_picture = Picture(user_id=resp, image="이미지 url", description=None)

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

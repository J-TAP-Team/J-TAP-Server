import datetime

from app.main import db
from app.main.model.picture import Picture
from .auth_helper import Auth


def upload_new_picture(request):

    resp = Auth.get_user_id_with_token(request)
    data = request.json

    # S3 업로드

    new_picture = Picture(user_id=resp, image="이미지 url", description=None)

    try:
        save_changes(new_picture)
    except Exception as e:
        response_object = {"status": "fail", "message": e}
        return response_object, 400

    response_object = {"status": "success", "message": "Successfully created."}
    return response_object, 201


def save_changes(data):
    try:
        db.session.add(data)
        db.session.commit()
    except Exception as e:
        print(e)

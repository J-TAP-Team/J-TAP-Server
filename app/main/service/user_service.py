import uuid
import datetime

from app.main import db
from app.main.model.user import User
from .auth_helper import Auth


def save_new_user(data):

    user = User.query.filter_by(email=data["email"]).first()

    if not user:
        new_user = User(
            public_id=str(uuid.uuid4()),
            email=data["email"],
            name=data["name"],
            password=data["password"],
            joined_at=datetime.datetime.utcnow(),
        )

        save_changes(new_user)

        response_object = {"status": "success", "message": "Successfully registered."}
        return response_object, 201
    else:
        response_object = {
            "status": "fail",
            "message": "User already exists. Please Log in.",
        }
        return response_object, 400


def get_all_users():
    return User.query.all()


def get_a_user(public_id):
    return User.query.filter_by(public_id=public_id).first()


def get_my_user(request):
    resp = Auth.get_user_id_with_token(request)
    return User.query.filter_by(user_id=resp).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()

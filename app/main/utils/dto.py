from typing_extensions import Required
from flask.globals import request
from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace("user", description="user related operations")
    user = api.model(
        "user",
        {
            "email": fields.String(required=True, description="user email address"),
            "name": fields.String(required=True, description="user username"),
            "password": fields.String(required=True, description="user password"),
            "public_id": fields.String(description="user public id"),
        },
    )


class AuthDto:
    api = Namespace("auth", description="authentication related operations")
    user_auth = api.model(
        "auth_details",
        {
            "email": fields.String(required=True, description="The email address"),
            "password": fields.String(required=True, description="The user password "),
        },
    )


class PictureDto:
    api = Namespace("picture", description="picture related operations")
    picture = api.model(
        "picture",
        {
            "user_id": fields.Integer(required=True, description="The user id"),
            "image": fields.String(required=True, description="The image url"),
            "description": fields.String(description="The description of Picture"),
        },
    )

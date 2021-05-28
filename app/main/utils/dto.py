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
            "picture_id": fields.Integer(description="The Picture Id"),
            "user_id": fields.Integer(description="User Id"),
            "image": fields.String(description="The image url"),
            "filename": fields.String(description="The filename of image"),
            "description": fields.String(description="The description of Picture"),
            "created_at": fields.DateTime(description="The creation datetime"),
        },
    )


class GalleryDto:
    api = Namespace("gallery", description="gallery related operations")
    gallery = api.model(
        "gallery",
        {
            "gallery_id": fields.Integer(description="The Gallery Id"),
            "user_id": fields.Integer(description="User Id"),
            "name": fields.String(description="The name of gallery"),
            "description": fields.String(description="The description of Gallery"),
            "created_at": fields.DateTime(description="The creation datetime"),
        },
    )


class DetailGalleryDto:
    api = Namespace(
        "detailed_gallery", description="detailed gallery related operations"
    )
    gallery = api.model(
        "detailed_gallery",
        {
            "gallery_id": fields.Integer(description="The Gallery Id"),
            "user_id": fields.Interger(description="User id"),
            "name": fields.String(description="The name of gallery"),
            "description": fields.String(description="The description of Gallery"),
            "created_at": fields.DateTime(description="The creation datetime"),
            "pictures": fields.List(description="The list of pictures"),
            "like": fields.Integer(description="Count of likes"),
            "isLiked": fields.Boolean(description="Is the user like this gallery"),
        },
    )


class CommentDto:
    api = Namespace("comment", description="comment related operations")
    comment = api.model(
        "comment",
        {
            "comment_id": fields.Integer(description="The Comment Id"),
            "user_id": fields.Integer(description="User Id"),
            "gallery_id": fields.Integer(description="Gallery Id"),
            "comment": fields.String(description="Comment contents"),
            "created_at": fields.DateTime(description="The creation datetime"),
        },
    )


class LikesDto:
    api = Namespace("likes", description="likes related operations")
    likes = api.model(
        "likes",
        {
            "likes_id": fields.Integer(description="The Comment Id"),
            "user_id": fields.Integer(description="User Id"),
            "gallery_id": fields.Integer(description="Gallery Id"),
            "created_at": fields.DateTime(description="The creation datetime"),
        },
    )


class LinkedDto:
    api = Namespace("linked", description="link related operations")
    linked = api.model(
        "linked",
        {
            "linked_id": fields.Integer(description="The Comment Id"),
            "user_id": fields.Integer(description="User Id"),
            "picture_id": fields.Integer(description="Picture Id"),
        },
    )

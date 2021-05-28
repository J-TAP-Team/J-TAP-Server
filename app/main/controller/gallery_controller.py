from app.main.service.comment_service import get_all_comments_on_this_gallery
import re

from flask import request
from flask_restplus import Resource

from ..service.gallery_service import *
from ..utils.dto import GalleryDto, CommentDto

from app.main.utils.decorator import token_required


api = GalleryDto.api
_gallery = GalleryDto.gallery
_comment = CommentDto.comment


@api.route("")
class GalleryList(Resource):
    @token_required
    @api.doc("list_of_gallery")
    @api.marshal_list_with(_gallery)
    @api.doc("get list of gallery")
    def get(self):
        return get_all_galleries(request=request)

    @token_required
    @api.response(201, "Gallery successfully uploaded")
    @api.doc("create a new gallery")
    @api.expect(_gallery, validate=False)
    def post(self):
        return create_new_gallery(request=request)


@api.route("/picture")
class Picture(Resource):
    @token_required
    @api.response(201, "Picture successfully Added")
    @api.doc("add picture to gallery")
    def post(self):
        return add_pictures(request=request)

    @token_required
    @api.response(404, "Gallery not fount")
    @api.doc("except picture in gallery")
    def delete(self):
        return except_pictures(request=request)


@api.route("/<id>")
@api.param("id", "The Gallery identifier")
@api.response(404, "Gallery not found")
class Gallery(Resource):
    @token_required
    @api.doc("get a gallery")
    def get(self, id):
        return get_a_gallery(request=request, id=id)

    @token_required
    @api.doc("modify a gallery")
    @api.marshal_with(_gallery)
    def put(self, id):
        return update_gallery(request=request, id=id)

    @token_required
    @api.doc("delete a gallery")
    @api.marshal_with(_gallery)
    def delete(self, id):
        return delete_gallery(request=request, id=id)


@api.route("/<id>/comments")
@api.param("id", "The Gallery identifier")
@api.response(404, "Gallery not found")
class Comments(Resource):
    @token_required
    @api.marshal_list_with(_comment)
    @api.doc("get all comments on this gallery")
    def get(self, id):
        return get_all_comments_on_this_gallery(request=request, id=id)


@api.route("/like")
class Likes(Resource):
    @token_required
    @api.doc("Click a like button of this Gallery")
    def post(self):
        return like_this_gallery(request=request)

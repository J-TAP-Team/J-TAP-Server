from flask import request
from flask_restplus import Resource

from ..utils.dto import GalleryDto

from app.main.utils.decorator import token_required


api = GalleryDto.api
_gallery = GalleryDto.picture


@api.route("")
class GalleryList(Resource):
    @token_required
    @api.doc("list_of_gallery")
    @api.marshal_list_with(_gallery, envelope="data")
    @api.doc("get list of gallery")
    def get(self):
        pass

    @token_required
    @api.response(201, "Gallery successfully uploaded")
    @api.doc("create a new gallery")
    @api.expect(_gallery, validate=False)
    def post(self):
        pass


@api.route("/<id>")
@api.param("id", "The Gallery identifier")
@api.response(404, "Gallery not found")
class Gallery(Resource):
    @token_required
    @api.doc("get a gallery")
    @api.marshal_with(_gallery)
    def get(self, id):
        pass

    @token_required
    @api.doc("modify a gallery")
    @api.marshal_with(_gallery)
    def put(self, id):
        pass

    @token_required
    @api.doc("delete a gallery")
    @api.marshal_with(_gallery)
    def delete(self, id):
        pass


@api.route("/<id>/comments")
@api.param("id", "The Gallery identifier")
@api.response(404, "Gallery not found")
class Comments(Resource):
    @token_required
    @api.doc("get a comments of this gallery")
    @api.marshal_with(_gallery)
    def get(self, id):
        pass

    @token_required
    @api.doc("get a gallery")
    @api.marshal_with(_gallery)
    def post(self, id):
        pass


@api.route("/like")
class Likes(Resource):
    @token_required
    @api.doc("Click a like button of this Gallery")
    @api.marshal_with(_gallery)
    def post(self, id):
        pass

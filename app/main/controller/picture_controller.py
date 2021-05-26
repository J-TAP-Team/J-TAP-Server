from flask import request
from flask_restplus import Resource

from ..utils.dto import PictureDto

from app.main.utils.decorator import token_required


api = PictureDto.api
_picture = PictureDto.picture


@api.route("/")
class PictureList(Resource):
    @token_required
    @api.doc("list_of_my_pictures")
    @api.marshal_list_with(_picture, envelope="data")
    @api.doc("get list of my pictures")
    def get(self):
        pass

    @token_required
    @api.response(201, "Picture successfully uploaded")
    @api.doc("upload a new picture")
    @api.expect(_picture, validate=True)
    def post(self):
        pass


@api.route("/<id>")
@api.param("id", "The Picture identifier")
@api.response(404, "Picture not found")
class Diary(Resource):
    @token_required
    @api.doc("get a picture")
    @api.marshal_with(_picture)
    def get(self, id):
        pass

    @token_required
    @api.doc("modify a picture")
    @api.marshal_with(_picture)
    def put(self, id):
        pass

    @token_required
    @api.doc("delete a picture")
    @api.marshal_with(_picture)
    def delete(self, id):
        pass

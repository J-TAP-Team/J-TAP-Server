from flask import request
from flask_restplus import Resource

from ..utils.dto import PictureDto
from ..service.picture_service import *

from app.main.utils.decorator import token_required


api = PictureDto.api
_picture = PictureDto.picture


@api.route("")
class PictureList(Resource):
    @token_required
    @api.doc("list_of_my_pictures")
    @api.marshal_list_with(_picture, envelope="data")
    @api.doc("get list of my pictures")
    def get(self):
        return get_all_pictures(request=request)

    @token_required
    @api.response(201, "Picture successfully uploaded")
    @api.doc("upload a new picture")
    @api.expect(_picture, validate=True)
    def post(self):
        return upload_new_picture(request=request)


@api.route("/<id>")
@api.param("id", "The Picture identifier")
@api.response(404, "Picture not found")
class Diary(Resource):
    @token_required
    @api.doc("get a picture")
    @api.marshal_with(_picture)
    def get(self, id):
        return get_a_picture(request=request, id=id)

    @token_required
    @api.doc("modify a picture")
    @api.marshal_with(_picture)
    def put(self, id):
        return update_picture(request=request, id=id)

    @token_required
    @api.doc("delete a picture")
    @api.marshal_with(_picture)
    def delete(self, id):
        return delete_picture(request=request, id=id)

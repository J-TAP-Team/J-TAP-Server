import re
from app.main.service.comment_service import *
from flask import request
from flask_restplus import Resource

from ..utils.dto import CommentDto

from app.main.utils.decorator import token_required


api = CommentDto.api
_comment = CommentDto.comment


@api.route("")
@api.response(404, "Gallery not found")
class Comments(Resource):
    @token_required
    @api.doc("get a gallery")
    @api.marshal_with(_comment)
    def post(self):
        return create_comment(request=request, id=id)


@api.route("/<id>")
@api.param("id", "The Comment identifier")
@api.response(404, "Comment not found")
class DetailComments(Resource):
    @token_required
    @api.doc("delete a comment")
    @api.marshal_with(_comment)
    def delete(self, id):
        return delete_comment(request=request, id=id)

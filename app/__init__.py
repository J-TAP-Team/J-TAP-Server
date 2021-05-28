from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.picture_controller import api as picture_ns
from .main.controller.gallery_controller import api as gallery_ns
from .main.controller.comment_controller import api as comment_ns

blueprint = Blueprint("api", __name__)

api = Api(
    blueprint,
    title="JTAP API",
    version="1.0",
    description="flask jtap server api",
)

api.add_namespace(user_ns, path="/user")
api.add_namespace(auth_ns)
api.add_namespace(picture_ns, path="/picture")
api.add_namespace(gallery_ns, path="/gallery")
api.add_namespace(comment_ns, path="/comment")

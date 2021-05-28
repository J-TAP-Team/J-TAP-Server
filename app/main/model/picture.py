from .. import db
import datetime
from .user import User


class Picture(db.Model):
    __tablename__ = "picture"

    picture_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.user_id, ondelete="CASCADE"))
    image = db.Column(db.String(100), unique=True)
    filename = db.Column(db.String(100), unique=True)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, nullable=False)

    user = db.relationship("User", backref=db.backref("picture_set", cascade="delete"))

    def __init__(self, user_id, image, filename, description):
        self.user_id = user_id
        self.image = image
        self.filename = filename
        self.description = description
        self.created_at = datetime.datetime.today()

    def __repr__(self):
        return "<Picture '{}'>".format(self.picture_id)

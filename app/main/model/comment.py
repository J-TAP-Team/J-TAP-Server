from .. import db
import datetime
from .user import User
from .gallery import Gallery


class Comment(db.Model):
    __tablename__ = "comment"

    comment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    gallery_id = db.Column(
        db.Integer,
        db.ForeignKey(Gallery.gallery_id, ondelete="CASCADE"),
        nullable=False,
    )
    user_id = db.Column(db.Integer, db.ForeignKey(User.user_id, ondelete="CASCADE"))
    comment = db.Column(db.Text)
    created_at = db.Column(db.DateTime, nullable=False)

    gallery = db.relationship(
        "Gallery", backref=db.backref("comment_set", cascade="delete")
    )
    user = db.relationship("User", backref=db.backref("comment_set", cascade="delete"))

    def __init__(self, gallery_id, user_id, comment):
        self.gallery_id = gallery_id
        self.user_id = user_id
        self.comment = comment
        self.created_at = datetime.datetime.today()

    def __reqr__(self):
        return "<Comment '{}'>".format(self.comment_id)

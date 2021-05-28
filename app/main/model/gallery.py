from .. import db
import datetime
from .user import User
from .picture import Picture


class Gallery(db.Model):
    __tablename__ = "gallery"

    gallery_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.user_id, ondelete="CASCADE"))
    name = db.Column(db.String(50))
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, nullable=False)

    user = db.relationship("User", backref=db.backref("gallery_set", cascade="delete"))

    def __init__(self, user_id, name, description):
        self.user_id = user_id
        self.name = name
        self.description = description
        self.created_at = datetime.datetime.today()

    def __repr__(self):
        return "<Gallery '{}'>".format(self.gallery_id)


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


class Likes(db.Model):
    __tablename__ = "likes"

    likes_id = db.Column(db.Integer, primary_key=True)
    gallery_id = db.Column(
        db.Integer,
        db.ForeignKey(Gallery.gallery_id, ondelete="CASCADE"),
        nullable=False,
    )
    user_id = db.Column(db.Integer, db.ForeignKey(User.user_id, ondelete="CASCADE"))
    created_at = db.Column(db.DateTime, nullable=False)

    gallery = db.relationship(
        "Gallery", backref=db.backref("likes_set", cascade="delete")
    )
    user = db.relationship("User", backref=db.backref("user_set", cascade="delete"))

    def __init__(self, gallery_id, user_id):
        self.gallery_id = gallery_id
        self.user_id = user_id
        self.created_at = datetime.datetime.today()

    def __repr__(self):
        return "<Likes '{}'>".format(self.likes_id)


class LinkedGalleryPicture(db.Model):
    __tablename__ = "linkedgallerypicture"

    linked_id = db.Column(db.Integer, primary_key=True)
    gallery_id = db.Column(
        db.Integer, db.ForeignKey(Gallery.gallery_id, ondelete="CASCADE")
    )
    picture_id = db.Column(
        db.Integer, db.ForeignKey(Picture.picture_id, ondelete="CASCADE")
    )

    gallery = db.relationship(
        "Gallery", backref=db.backref("linkedgallerypicture_set", cascade="delete")
    )
    picture = db.relationship(
        "Picture", backref=db.backref("linkedgallerypicture_set", cascade="delete")
    )

    def __init__(self, gallery_id, picture_id):
        self.gallery_id = gallery_id
        self.picture_id = picture_id

    def __repr__(self):
        return "<LinkedGalleryPicture> '{}'>".format(self.linked_id)

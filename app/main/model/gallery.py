from .. import db
import datetime
from .user import User
from .picture import Picture


class Gallery(db.Model):
    __tablename__ = "gallery"

    gallery_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.user_id), nullable=False)
    name = db.Column(db.String(50))
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, nullable=False)

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
        db.Integer, db.ForeignKey(Gallery.gallery_id), nullable=False
    )
    user_id = db.Column(db.Integer, db.ForeignKey(User.user_id), nullable=False)
    comment = db.Column(db.Text)
    created_at = db.Column(db.DateTime, nullable=False)

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
        db.Integer, db.ForeignKey(Gallery.gallery_id), nullable=False
    )
    user_id = db.Column(db.Integer, db.ForeignKey(User.user_id), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

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
        db.Integer, db.ForeignKey(Gallery.gallery_id), nullable=False
    )
    picture_id = db.Column(
        db.Integer, db.ForeignKey(Picture.picture_id), nullable=False
    )

    def __init__(self, gallery_id, picture_id):
        self.gallery_id = gallery_id
        self.picture_id = picture_id

    def __repr__(self):
        return "<LinkedGalleryPicture> '{}'>".format(self.linked_id)

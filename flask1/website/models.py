from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Profile(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    fname = db.Column(db.String(50))
    lname = db.Column(db.String(50))
    position = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(150),unique=True)
    password = db.Column(db.String(150))
    firstname = db.Column(db.String(150))
    profile_info = db.relationship('Profile')
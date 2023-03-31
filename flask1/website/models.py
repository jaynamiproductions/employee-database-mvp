from . import db
from flask_login import UserMixin
import datetime

class Demo(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    fname = db.Column(db.String(50))
    lname = db.Column(db.String(50))
    position = db.Column(db.String(50))
    date = db.Column(db.String(50), default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Cert(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    acls_cert = db.Column(db.Integer)
    annual_trophon = db.Column(db.String(50))
    date = db.Column(db.String(50), default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Form(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    kronos = db.Column(db.String(50))
    kronosdata = db.Column(db.LargeBinary)

    performance = db.Column(db.String(50))
    performancedata = db.Column(db.LargeBinary)

    attestation = db.Column(db.String(50))
    attestationdata = db.Column(db.LargeBinary)

    ivcontrast = db.Column(db.String(50))
    ivcontrastdata = db.Column(db.LargeBinary)

    supportperform = db.Column(db.String(50))
    supportperformdata = db.Column(db.LargeBinary)

    couns = db.Column(db.String(50))
    counsdata = db.Column(db.LargeBinary)

    hybrid = db.Column(db.String(50))
    hybriddata = db.Column(db.LargeBinary)

    date = db.Column(db.String(50), default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(150),unique=True)
    password = db.Column(db.String(150))
    demo_info = db.relationship('Demo')
    cert_info = db.relationship('Cert')
    form_info = db.relationship('Form')


from email.policy import default
from enum import unique
from datetime import datetime
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    fname = db.Column(db.String(150), unique=False)
    lname = db.Column(db.String(150), unique=False)
    password = db.Column(db.String(250), unique=False)
    date_create = db.Column(db.DateTime(timezone=True), default=func.now())



class Prefences(db.Model, UserMixin):
    user_id = db.Column(db.String(150), primary_key=True)
    av_api = db.Column(db.String, unique=True)
    date_create = db.Column(db.DateTime(timezone=True), default=func.now())

from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import datetime

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    number = db.Column(db.String(150))
    firstName = db.Column(db.String(150))
    status = db.Column(db.String(120))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

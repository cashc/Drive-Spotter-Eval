from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import string, random

db = SQLAlchemy()
SIMPLE_CHARS = string.ascii_letters + string.digits


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(45))
    lastname = db.Column(db.String(45))
    username = db.Column(db.String(120), unique=True)
    hash = db.Column(db.String(64))

    def check_password(self, password):
        return check_password_hash(self.hash, password)

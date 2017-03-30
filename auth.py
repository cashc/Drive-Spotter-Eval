from __init__ import db
from flask import request, Response
from functools import wraps
from models import *


def check_auth(username, password):
    user = db.session.query(User).filter_by(username=username).first()
    if type(user) is User:
        if user.check_password(password):
            return True
    return False


def authenticate():
    return Response(
        'Could not verify your for that URL.\n'
        'You have to login with proper credentials', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'})


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)

    return decorated

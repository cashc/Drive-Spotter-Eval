from flask import Flask, render_template, request, Response
from functools import wraps
from flask_sqlalchemy import SQLAlchemy
from models import User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/cashc'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


def check_auth(username, password):
    user = db.session.query(User).filter_by(email=username).first()
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


@app.route('/')
@requires_auth
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run()

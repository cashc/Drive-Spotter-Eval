from __init__ import app, db
from flask import render_template
from auth import *


@app.route('/')
@requires_auth
def home():
    allUsers = db.session.query(User).all()
    return render_template('home.html', users=allUsers)
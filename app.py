from __init__ import *
from flask import render_template
from auth import *


@app.route('/')
@requires_auth
def home():
    return render_template('home.html')
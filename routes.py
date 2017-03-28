from flask import Flask, render_template
from auth import *

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/cashc'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route('/')
@requires_auth
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run()

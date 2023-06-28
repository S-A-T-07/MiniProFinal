from flask import Blueprint

home = Blueprint("home", __name__)

@home.route('/')
def homepage():
    return "<p>This is the home page</p>"

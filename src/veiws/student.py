from flask import Blueprint

StudentViews = Blueprint("StudentViews", __name__)

@StudentViews.route("/")
def home():
    return "<H1>This a student Homepage</H1>"

@StudentViews.route("/result")
def result():
    return "<H1>This a student result page</H1>"

@StudentViews.route("/filter_by")
def filter_by():
    return "<H1>This a student Filter page</H1>"
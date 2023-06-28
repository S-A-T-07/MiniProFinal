from flask import Blueprint

TeacherViews = Blueprint("TeacherViews", __name__)

@TeacherViews.route("/")
def home():
    return "<H1>This a Teacher Homepage</H1>"

@TeacherViews.route("/upload")
def upload():
    return "<H1>This a Upload Homepage</H1>"

@TeacherViews.route("/filter_by")
def filter_by():
    return "<H1>This a Teacher filter_by page</H1>"
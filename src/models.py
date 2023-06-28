from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class UserBase(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    studentbase = db.relationship('StudentBase')
    teacherbase = db.relationship('TeacherBase')

class StudentBase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    RegNo = db.Column(db.String(150))
    name = db.Column(db.String(150))
    batch = db.Column(db.Integer)
    result_id = db.relationship('Result.id')
    userbase_id = db.Column(db.Integer, db.ForeignKey('UserBase.id'))

class TeacherBase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    subject = db.relationship('Subject')
    user_id = db.Column(db.Integer, db.ForeignKey('UserBase.id'))


class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    results_id = db.relationship('Results')
    teacher_id = db.Column(db.Integer, db.ForeignKey('TeacherBase.id'))

class Results(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    grade = db.Column(db.String(2))
    studentbase_id = db.Column(db.Integer, db.ForeignKey('StudentBase.id'))
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'))
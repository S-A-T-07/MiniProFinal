from . import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    students = db.relationship('Student', backref='user', lazy=True)
    teachers = db.relationship('Teacher', backref='user', lazy=True)


class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    reg_no = db.Column(db.String(150))
    name = db.Column(db.String(150))
    batch = db.Column(db.Integer)
    result_id = db.Column(db.Integer, db.ForeignKey('results.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


class Teacher(db.Model):
    __tablename__ = 'teachers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    subject_id = db.Column(db.Integer, db.ForeignKey('subjects.id'))


class Subject(db.Model):
    __tablename__ = 'subjects'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    results = db.relationship('Result', backref='subject', lazy=True)


class Result(db.Model):
    __tablename__ = 'results'
    id = db.Column(db.Integer, primary_key=True)
    grade = db.Column(db.String(2))
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
    subject_id = db.Column(db.Integer, db.ForeignKey('subjects.id'))

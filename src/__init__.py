from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


db = SQLAlchemy()
DB_NAME = "database.db"

def MainApp():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .veiws.home import home
    from .veiws.student import StudentViews
    from .veiws.teacher import TeacherViews

    app.register_blueprint(home, url_prefix='/')
    app.register_blueprint(StudentViews, url_prefix='/student')
    app.register_blueprint(TeacherViews, url_prefix='/teacher')

    from .models import UserBase

    with app.app_context():
        db.create_all()

    return app

def create_database(app):
    if not path.exists('src/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
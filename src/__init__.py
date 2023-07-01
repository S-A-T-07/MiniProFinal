# built-in module
from os import path

# third party libraries
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


db = SQLAlchemy()
DB_NAME = "database.db"


def MainApp():

    # project configuration
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    # import for the blueprints
    from .veiws.home import home
    from .veiws.student import StudentViews
    from .veiws.teacher import TeacherViews
    from .views.auth import auth_blueprint

    # blueprint mapping for the web application
    app.register_blueprint(home, url_prefix='/')    # url prefix for home
    app.register_blueprint(StudentViews, url_prefix='/student') # url prefix for student
    app.register_blueprint(TeacherViews, url_prefix='/teacher') # url prefix for teacher
    app.register_blueprint(auth_blueprint, url_prefix='/auth')  # url prefix for auth

    # import the models 
    from .models import User

    with app.app_context():
        db.create_all()

    # user login
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


# create a the database if not exist
def create_database(app):
    if not path.exists(DB_NAME):
        with app.app_context():
            db.create_all()
        print('Created Database!')
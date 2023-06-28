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
    from .views.auth import auth_blueprint

    app.register_blueprint(home, url_prefix='/')
    app.register_blueprint(StudentViews, url_prefix='/student')
    app.register_blueprint(TeacherViews, url_prefix='/teacher')
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .models import User

    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    if not path.exists(DB_NAME):
        with app.app_context():
            db.create_all()
        print('Created Database!')
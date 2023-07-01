from flask import Blueprint, render_template, redirect, request, flash, url_for
from flask_login import login_user, logout_user, login_required, current_user
from models import User

auth_blueprint = Blueprint('auth', __name__, url_prefix='/auth')


@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        GivenKey = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and user.password == password:
            if user.is_admin == GivenKey:
                login_user(user)
                flash('Logged in successfully!', 'success')
                return redirect(url_for('auth.protected'))
        else:
            flash('Invalid email or password', 'error')
    return render_template('login.html')


@auth_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('auth.login'))


@auth_blueprint.route('/protected')
@login_required
def protected():
    return render_template('protected.html', current_user=current_user)

from flask import render_template, redirect, url_for
from flask_login import login_user, logout_user
from forms import LoginForm

from models import User
from server import app

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user_data = {
            'email': form.email.data,
            'password': form.password.data
        }
        user = User.get_by_email(user_data['email'])
        if user is None:
            raise ValueError('This user doesn\'t exist.')
        if user.check_password(user_data['password']):
            login_user(user, remember=True)
            return redirect(url_for('admin_dashboard'))
        else:
            raise ValueError('Invalid password.')
    logout_user()
    return render_template('auth/login.html', form=form)
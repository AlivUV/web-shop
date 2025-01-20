from flask import render_template, redirect, url_for
from flask_login import current_user, login_user, logout_user
from forms import SignupForm

from models import User
from models import Client
from server import app

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        user_data = {
            'name': form.name.data,
            'email': form.email.data,
            'password': form.password.data
        }
        user = User.get_by_email(user_data)
        if user is not None:
            raise ValueError('This email is already being used by another user.')
        if not user_data['password'] == form.confirm_password.data:
            raise ValueError(f'Passwords must match. {user_data['password']} {form.confirm_password.data}')
        else:
            user = User.create_user(**user_data)
            return redirect(url_for('login'))
    logout_user()
    return render_template('auth/signup.html', form=form)
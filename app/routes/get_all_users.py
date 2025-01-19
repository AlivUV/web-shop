from flask import render_template

from server import app
from models import User


@app.route('/user/get-all')
def get_all_users():
    all_users = User.get_all()
    return render_template('users.html', users=all_users)
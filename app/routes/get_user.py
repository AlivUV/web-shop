from flask import render_template

from server import app
from models import User


@app.route('/user/get/<int:id>')
def users(id):
    user = User.get_by_id(id)
    if not user:
        return render_template('users.html', user='This user doesn\'t exist.')
    return render_template('users.html', user=user)
from flask import redirect, url_for
from flask_login import login_required, logout_user

from server import app

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
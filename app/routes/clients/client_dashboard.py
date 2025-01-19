from flask import render_template
from flask_login import login_required

from server import app

@app.route('/shop')
@login_required
def client_dashboard():
    return render_template('clients/client_dashboard.html')
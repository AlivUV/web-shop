from flask import render_template
from flask_login import login_required

from decorators import admin_required
from server import app

@app.route('/admin/dashboard')
@login_required
@admin_required
def admin_dashboard():
    return render_template('admin/admin_dashboard.html')
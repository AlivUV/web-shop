from functools import wraps

from flask import abort, redirect, url_for
from flask_login import current_user

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kws):
        if not current_user.is_admin:
            return redirect(url_for('client_dashboard'))
        return f(*args, **kws)
    return decorated_function
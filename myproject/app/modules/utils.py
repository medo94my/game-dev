from functools import wraps
from flask import session ,flash, redirect, url_for

def is_logged_in(f):
    @wraps(f)
    def fn(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login', 'danger')
            return redirect(url_for('login'))
    return fn
from functools import wraps
from flask import  render_template,request,jsonify

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        # if user is not logged in, redirect to login page
        return render_template('demo.html', data={})
    return wrap
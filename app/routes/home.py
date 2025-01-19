from flask import render_template

from server import app

@app.route('/')
@app.route('/home')
@app.route('/index')
def home():
    return render_template('public/index.html')
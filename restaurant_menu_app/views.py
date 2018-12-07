from flask import render_template
from restaurant_menu_app import app


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

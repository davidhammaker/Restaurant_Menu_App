from flask import render_template, url_for
from restaurant_menu_app import app
from restaurant_menu_app.models import Restaurant


@app.route('/')
@app.route('/home')
def home():
    restaurants = Restaurant.query.all()
    return render_template('home.html', restaurants=restaurants)

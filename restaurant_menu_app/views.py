from flask import render_template, url_for, redirect
from restaurant_menu_app import app
from restaurant_menu_app.models import Restaurant, MenuItem
from restaurant_menu_app.forms import RestaurantForm


@app.route('/')
@app.route('/home')
def home():
    restaurants = Restaurant.query.all()
    return render_template('home.html', restaurants=restaurants)


@app.route('/<string:restaurant_name>')
def restaurant(restaurant_name):
    restaurant = Restaurant.query.filter_by(name=restaurant_name).first()
    if not restaurant:
        return redirect(url_for('home'))
    items = restaurant.menu_items
    return render_template('restaurant.html', restaurant=restaurant, items=items)


@app.route('/new_restaurant')
def new_restaurant():
    form = RestaurantForm()
    return render_template('new_restaurant.html', form=form, title='New Restaurant')

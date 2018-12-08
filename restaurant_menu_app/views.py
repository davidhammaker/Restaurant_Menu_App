from flask import render_template, url_for, redirect
from restaurant_menu_app import app, db
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


@app.route('/new_restaurant', methods=['GET', 'POST'])
def new_restaurant():
    form = RestaurantForm()
    if form.validate_on_submit():
        new_restaurant = Restaurant(name=form.name.data)
        db.session.add(new_restaurant)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('new_restaurant.html', form=form, title='New Restaurant')

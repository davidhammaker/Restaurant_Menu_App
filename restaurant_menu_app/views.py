from flask import render_template, url_for, redirect, flash
from restaurant_menu_app import app, db
from restaurant_menu_app.models import Restaurant, MenuItem
from restaurant_menu_app.forms import RestaurantForm, DeleteConfirmForm


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
        flash(f'"{form.name.data}" has been added!', 'good')
        return redirect(url_for('home'))
    return render_template('new_restaurant.html', form=form, title='New Restaurant')


@app.route('/<string:restaurant_name>/delete_confirm')
def delete_confirm(restaurant_name):
    restaurant = Restaurant.query.filter_by(name=restaurant_name).first()
    if not restaurant:
        return redirect(url_for('home'))
    form = DeleteConfirmForm()
    return render_template('delete_confirm.html', form=form, restaurant=restaurant)


@app.route('/<string:restaurant_name>/delete', methods=['POST'])
def delete(restaurant_name):
    restaurant = Restaurant.query.filter_by(name=restaurant_name).first()
    form = DeleteConfirmForm()
    if form.validate_on_submit():
        if form.confirm.data == 'Delete':
            db.session.delete(restaurant)
            db.session.commit()
            flash(f'"{restaurant.name}" has been deleted.', 'good')
        else:
            flash(f'Nothing has been deleted.', 'neutral')
        return redirect(url_for('home'))
    else:
        flash('Please select an option and try again.', 'neutral')
        return redirect(url_for('delete_confirm', restaurant_name=restaurant_name))

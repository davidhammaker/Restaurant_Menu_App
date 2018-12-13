from flask import render_template, url_for, redirect, flash, request, Blueprint, abort
from restaurant_menu_app import db
from restaurant_menu_app.models import Restaurant
from restaurant_menu_app.forms import RestaurantForm, DeleteConfirmForm

restaurants = Blueprint('restaurants', __name__)


@restaurants.route('/<string:restaurant_name>')
def restaurant(restaurant_name):
    restaurant = Restaurant.query.filter_by(name=restaurant_name).first()
    if not restaurant:
        abort(404)
    items = restaurant.menu_items
    return render_template('restaurant.html', restaurant=restaurant, items=items, title=restaurant_name)


@restaurants.route('/new_restaurant', methods=['GET', 'POST'])
def new_restaurant():
    form = RestaurantForm()
    if form.validate_on_submit():
        new_restaurant = Restaurant(name=form.name.data)
        db.session.add(new_restaurant)
        db.session.commit()
        flash(f'"{form.name.data}" has been added!', 'good')
        return redirect(url_for('main.home'))
    return render_template('new_restaurant.html', form=form, title='New Restaurant')


@restaurants.route('/<string:restaurant_name>/edit', methods=['GET', 'POST'])
def edit(restaurant_name):
    form = RestaurantForm()
    restaurant = Restaurant.query.filter_by(name=restaurant_name).first()
    if not restaurant:
        abort(404)
    if form.validate_on_submit():
        if restaurant.name != form.name.data:
            check_restaurant = Restaurant.query.filter_by(name=form.name.data).first()
            if check_restaurant:
                flash(f'"{form.name.data}" already exists.', 'bad')
                return redirect(url_for('items.edit_item', restaurant_name=restaurant.name))
        restaurant.name = form.name.data
        db.session.commit()
        flash(f'"{form.name.data}" has been updated!', 'good')
        return redirect(url_for('restaurants.restaurant', restaurant_name=restaurant.name))
    elif request.method == 'GET':
        form.name.data = restaurant.name
    return render_template('edit.html', form=form, title='Edit Restaurant')


@restaurants.route('/<string:restaurant_name>/delete_confirm')
def delete_confirm(restaurant_name):
    restaurant = Restaurant.query.filter_by(name=restaurant_name).first()
    if not restaurant:
        abort(404)
    form = DeleteConfirmForm()
    return render_template('delete_confirm.html', form=form, restaurant=restaurant, title=f'Delete "{restaurant_name}"')


@restaurants.route('/<string:restaurant_name>/delete', methods=['POST'])
def delete(restaurant_name):
    restaurant = Restaurant.query.filter_by(name=restaurant_name).first()
    form = DeleteConfirmForm()
    if not restaurant:
        abort(404)
    if form.validate_on_submit():
        if form.confirm.data == 'Delete':
            db.session.delete(restaurant)
            db.session.commit()
            flash(f'"{restaurant.name}" has been deleted.', 'good')
        else:
            flash(f'Nothing has been deleted.', 'neutral')
        return redirect(url_for('main.home'))
    else:
        flash('Please select an option and try again.', 'neutral')
        return redirect(url_for('restaurants.delete_confirm', restaurant_name=restaurant_name))

from flask import render_template, url_for, redirect, flash
from restaurant_menu_app import app, db
from restaurant_menu_app.models import Restaurant, MenuItem
from restaurant_menu_app.forms import RestaurantForm, DeleteConfirmForm, MenuItemsForm


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


@app.route('/<string:restaurant_name>/add_item', methods=['GET', 'POST'])
def add_item(restaurant_name):
    form = MenuItemsForm()
    restaurant = Restaurant.query.filter_by(name=restaurant_name).first()
    form.restaurant_id.data = restaurant.id
    if form.validate_on_submit():
        check_item = MenuItem.query.filter_by(name=form.name.data, restaurant_id=form.restaurant_id.data).first()
        if check_item:
            flash(f'"{form.name.data}" is already on the menu.', 'bad')
            return redirect(url_for('add_item', restaurant_name=restaurant_name))
        else:
            new_item = MenuItem(name=form.name.data, course=form.course.data,
                            price=form.price.data, description=form.description.data,
                            restaurant_id=form.restaurant_id.data)
            db.session.add(new_item)
            db.session.commit()
            flash(f'"{form.name.data}" has been added!', 'good')
            return redirect(url_for('restaurant', restaurant_name=restaurant_name))
    return render_template('add_item.html', form=form, title='New Menu Item')

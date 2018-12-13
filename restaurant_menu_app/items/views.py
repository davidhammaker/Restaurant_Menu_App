from flask import render_template, url_for, redirect, flash, request, Blueprint, abort
from restaurant_menu_app import db
from restaurant_menu_app.models import Restaurant, MenuItem
from restaurant_menu_app.forms import DeleteConfirmForm, MenuItemsForm, EditItemForm

items = Blueprint('items', __name__)


@items.route('/<string:restaurant_name>/add_item', methods=['GET', 'POST'])
def add_item(restaurant_name):
    form = MenuItemsForm()
    restaurant = Restaurant.query.filter_by(name=restaurant_name).first()
    if not restaurant:
        abort(404)
    else:
        form.restaurant_id.data = restaurant.id
    if form.validate_on_submit():
        check_item = MenuItem.query.filter_by(name=form.name.data, restaurant_id=form.restaurant_id.data).first()
        if check_item:
            flash(f'"{form.name.data}" is already on the menu.', 'bad')
            return redirect(url_for('items.add_item', restaurant_name=restaurant_name))
        else:
            new_item = MenuItem(name=form.name.data, course=form.course.data,
                                price=form.price.data, description=form.description.data,
                                restaurant_id=form.restaurant_id.data)
            db.session.add(new_item)
            db.session.commit()
            flash(f'"{form.name.data}" has been added!', 'good')
            return redirect(url_for('restaurants.restaurant', restaurant_name=restaurant_name))
    return render_template('add_item.html', form=form, title='New Menu Item')


@items.route('/<string:restaurant_name>/edit_item/<string:item_name>', methods=['GET', 'POST'])
def edit_item(restaurant_name, item_name):
    form = EditItemForm()
    restaurant = Restaurant.query.filter_by(name=restaurant_name).first()
    menu_item = MenuItem.query.filter_by(name=item_name, restaurant_id=restaurant.id).first()
    if not restaurant or not menu_item:
        abort(404)
    else:
        form.restaurant_id.data = restaurant.id
    if form.validate_on_submit():
        if menu_item.name != form.name.data:
            check_item = MenuItem.query.filter_by(name=form.name.data, restaurant_id=form.restaurant_id.data).first()
            if check_item:
                flash(f'"{form.name.data}" is already on the menu.', 'bad')
                return redirect(url_for('items.edit_item', restaurant_name=restaurant.name, item_name=menu_item.name))
        menu_item.name = form.name.data
        menu_item.course = form.course.data
        menu_item.description = form.description.data
        menu_item.price = form.price.data
        db.session.commit()
        print(menu_item)
        flash(f'"{form.name.data}" has been updated!', 'good')
        return redirect(url_for('restaurants.restaurant', restaurant_name=restaurant.name))
    elif request.method == 'GET':
        form.name.data = menu_item.name
        form.course.data = menu_item.course
        form.description.data = menu_item.description
        form.price.data = menu_item.price
    return render_template('edit_item.html', form=form, title=f'Edit "{item_name}"')


@items.route('/<string:restaurant_name>/delete_item_confirm/<string:item_name>')
def delete_item_confirm(restaurant_name, item_name):
    restaurant = Restaurant.query.filter_by(name=restaurant_name).first()
    menu_item = MenuItem.query.filter_by(name=item_name, restaurant_id=restaurant.id).first()
    if not restaurant or not menu_item:
        abort(404)
    form = DeleteConfirmForm()
    return render_template('delete_item_confirm.html', form=form,
                           restaurant=restaurant, menu_item=menu_item,
                           title=f'Delete "{item_name}"')


@items.route('/<string:restaurant_name>/delete_item/<string:item_name>', methods=['POST'])
def delete_item(restaurant_name, item_name):
    menu_item = MenuItem.query.filter_by(name=item_name).first()
    form = DeleteConfirmForm()
    if form.validate_on_submit():
        if form.confirm.data == 'Delete':
            db.session.delete(menu_item)
            db.session.commit()
            flash(f'"{menu_item.name}" has been deleted.', 'good')
        else:
            flash(f'Nothing has been deleted.', 'neutral')
        return redirect(url_for('restaurants.restaurant', restaurant_name=restaurant_name))
    else:
        flash('Please select an option and try again.', 'neutral')
        return redirect(url_for('items.delete_item_confirm', restaurant_name=restaurant_name, item_name=item_name))

from flask import render_template, url_for, redirect, flash, request
from restaurant_menu_app import app, db
from restaurant_menu_app.models import Restaurant, MenuItem
from restaurant_menu_app.forms import RestaurantForm, DeleteConfirmForm, MenuItemsForm, EditItemForm


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
    return render_template('restaurant.html', restaurant=restaurant, items=items, title=restaurant_name)


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
    return render_template('delete_confirm.html', form=form, restaurant=restaurant, title=f'Delete "{restaurant_name}"')


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


@app.route('/<string:restaurant_name>/edit_item/<string:item_name>', methods=['GET', 'POST'])
def edit_item(restaurant_name, item_name):
    form = EditItemForm()
    restaurant = Restaurant.query.filter_by(name=restaurant_name).first()
    menu_item_search = MenuItem.query.filter_by(name=item_name, restaurant_id=restaurant.id).first()
    menu_item = MenuItem.query.get_or_404(menu_item_search.id)
    form.restaurant_id.data = restaurant.id
    if form.validate_on_submit():
        if menu_item.name != form.name.data:
            check_item = MenuItem.query.filter_by(name=form.name.data, restaurant_id=form.restaurant_id.data).first()
            if check_item:
                flash(f'"{form.name.data}" is already on the menu.', 'bad')
                return redirect(url_for('edit_item', restaurant_name=restaurant.name, item_name=menu_item.name))
        menu_item.name = form.name.data
        menu_item.course = form.course.data
        menu_item.description = form.description.data
        menu_item.price = form.price.data
        db.session.commit()
        print(menu_item)
        flash(f'"{form.name.data}" has been updated!', 'good')
        return redirect(url_for('restaurant', restaurant_name=restaurant.name))
    elif request.method == 'GET':
        form.name.data = menu_item.name
        form.course.data = menu_item.course
        form.description.data = menu_item.description
        form.price.data = menu_item.price
    return render_template('edit_item.html', form=form, title=f'Edit "{item_name}"')


@app.route('/<string:restaurant_name>/delete_item_confirm/<string:item_name>')
def delete_item_confirm(restaurant_name, item_name):
    restaurant = Restaurant.query.filter_by(name=restaurant_name).first()
    menu_item = MenuItem.query.filter_by(name=item_name, restaurant_id=restaurant.id).first()
    if not restaurant or not menu_item:
        return redirect(url_for('home'))
    form = DeleteConfirmForm()
    return render_template('delete_item_confirm.html', form=form,
                           restaurant=restaurant, menu_item=menu_item,
                           title=f'Delete "{item_name}"')


@app.route('/<string:restaurant_name>/delete_item/<string:item_name>', methods=['POST'])
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
        return redirect(url_for('restaurant', restaurant_name=restaurant_name))
    else:
        flash('Please select an option and try again.', 'neutral')
        return redirect(url_for('delete_item_confirm', restaurant_name=restaurant_name, item_name=item_name))


@app.route('/<string:restaurant_name>/edit', methods=['GET', 'POST'])
def edit(restaurant_name):
    form = RestaurantForm()
    restaurant_search = Restaurant.query.filter_by(name=restaurant_name).first()
    if not restaurant_search:
        return redirect('home.html')
    if form.validate_on_submit():
        if restaurant.name != form.name.data:
            check_restaurant = Restaurant.query.filter_by(name=form.name.data).first()
            if check_restaurant:
                flash(f'"{form.name.data}" already exists.', 'bad')
                return redirect(url_for('edit_item', restaurant_name=restaurant.name, item_name=menu_item.name))
        restaurant.name = form.name.data
        db.session.commit()
        flash(f'"{form.name.data}" has been updated!', 'good')
        return redirect(url_for('restaurant', restaurant_name=restaurant.name))
    elif request.method == 'GET':
        form.name.data = restaurant.name
    return render_template('edit.html', form=form, title='Edit Restaurant')

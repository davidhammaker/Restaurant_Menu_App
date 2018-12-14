from flask import jsonify, Blueprint, abort
from restaurant_menu_app.models import Restaurant, MenuItem
from restaurant_menu_app.jsons.utils import prep_item, prep_restaurant, prep_menu, prep_restaurants
from flask_login import login_required, current_user

jsons = Blueprint('json', __name__)


@jsons.route('/restaurants/<int:restaurant_id>/menu/JSON')
@login_required
def menu_json(restaurant_id):
    restaurant = Restaurant.query.get_or_404(restaurant_id)
    if restaurant.user != current_user:
        abort(403)
    menu = restaurant.menu_items
    return jsonify(restaurant=prep_restaurant(restaurant), menu=prep_menu(menu))


@jsons.route('/restaurants/JSON')
@login_required
def restaurants_json():
    restaurants = Restaurant.query.filter_by(private=False).all()
    return jsonify(restaurants=prep_restaurants(restaurants))


@jsons.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/JSON')
@login_required
def item_json(restaurant_id, menu_id):
    restaurant = Restaurant.query.get_or_404(restaurant_id)
    if restaurant.user != current_user:
        abort(403)
    menu_item = MenuItem.query.get_or_404(menu_id)
    return jsonify(restaurant=prep_restaurant(restaurant), menu_item=prep_item(menu_item))

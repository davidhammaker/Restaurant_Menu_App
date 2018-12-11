from flask import render_template, Blueprint
from restaurant_menu_app.models import Restaurant

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
def home():
    restaurants = Restaurant.query.all()
    return render_template('home.html', restaurants=restaurants)

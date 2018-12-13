import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('RESTAURANT_SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restaurantmenu.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from restaurant_menu_app.items.views import items
from restaurant_menu_app.jsons.views import jsons
from restaurant_menu_app.main.views import main
from restaurant_menu_app.restaurants.views import restaurants
from restaurant_menu_app.errors.handlers import errors
app.register_blueprint(items)
app.register_blueprint(jsons)
app.register_blueprint(main)
app.register_blueprint(restaurants)
app.register_blueprint(errors)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from restaurant_menu_app.config import Config

db = SQLAlchemy()

login_manager = LoginManager()
login_manager.login_view = 'github.login'
login_manager.login_message_category = 'neutral'


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    login_manager.init_app(app)

    from restaurant_menu_app.items.views import items
    from restaurant_menu_app.jsons.views import jsons
    from restaurant_menu_app.main.views import main
    from restaurant_menu_app.restaurants.views import restaurants
    from restaurant_menu_app.dance.utils import blueprint as dance
    from restaurant_menu_app.errors.handlers import errors
    app.register_blueprint(items)
    app.register_blueprint(jsons)
    app.register_blueprint(main)
    app.register_blueprint(restaurants)
    app.register_blueprint(dance, url_prefix="/login")
    app.register_blueprint(errors)

    return app

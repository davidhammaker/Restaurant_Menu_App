import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('RESTAURANT_SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restaurantmenu.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from restaurant_menu_app import views

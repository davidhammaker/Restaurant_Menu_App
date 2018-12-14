from flask import render_template, Blueprint, flash, redirect, url_for
from flask_login import login_required, logout_user
from restaurant_menu_app.models import Restaurant

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
def home():
    restaurants = Restaurant.query.all()
    return render_template('home.html', restaurants=restaurants)


@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have logged out.", "neutral")
    return redirect(url_for('main.home'))

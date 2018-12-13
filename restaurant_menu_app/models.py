from flask_dance.consumer.backend.sqla import OAuthConsumerMixin
from flask_login import UserMixin
from restaurant_menu_app import db


class Restaurant(db.Model):
    name = db.Column(db.String(80), nullable=False)
    id = db.Column(db.Integer, primary_key=True)
    menu_items = db.relationship('MenuItem', backref='restaurant', lazy=True)
    user_id = db.Column(db.String(256), db.ForeignKey('user.id'), nullable=False)
    private = db.Column(db.Boolean)

    def __repr__(self):
        return f"Restaurant('{self.name}', '{self.user.username}')"


class MenuItem(db.Model):
    name = db.Column(db.String(80), nullable=False)
    id = db.Column(db.Integer, primary_key=True)
    course = db.Column(db.String(250))
    description = db.Column(db.String(250))
    price = db.Column(db.String(8))
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)

    def __repr__(self):
        return f"MenuItem('{self.name}', '{self.course}', '{self.price}', '{self.restaurant.name}')"


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), unique=True)
    email = db.Column(db.String(256), unique=True)
    username = db.Column(db.String(256), unique=True)
    restaurants = db.relationship('Restaurant', backref='user', lazy=True)


class OAuth(OAuthConsumerMixin, db.Model):
    provider_user_id = db.Column(db.String(256), unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    user = db.relationship(User)

from restaurant_menu_app import db


class Restaurant(db.Model):
    name = db.Column(db.String(80), nullable=False)
    id = db.Column(db.Integer, primary_key=True)
    menu_items = db.relationship('MenuItem', backref='restaurant', lazy=True)

    def __repr__(self):
        return f"Restaurant('{self.name}')"


class MenuItem(db.Model):
    name = db.Column(db.String(80), nullable=False)
    id = db.Column(db.Integer, primary_key=True)
    course = db.Column(db.String(250))
    description = db.Column(db.String(250))
    price = db.Column(db.String(8))
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))

    def __repr__(self):
        return f"MenuItem('{self.name}', '{self.course}', '{self.price}')"

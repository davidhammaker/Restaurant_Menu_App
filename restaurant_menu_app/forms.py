from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, SubmitField, SelectField,
                     ValidationError, IntegerField, RadioField)
from restaurant_menu_app.models import Restaurant, MenuItem
from wtforms.validators import DataRequired, Length


class RestaurantForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=50)])
    submit = SubmitField('Submit')

    def validate_name(self, name):
        restaurant = Restaurant.query.filter_by(name=name.data).first()
        if restaurant:
            raise ValidationError('That restaurant already exists.')


class MenuItemsForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=50)])
    course = SelectField('Course', choices=[('Entree', 'Entree'),
                                            ('Appetizer', 'Appetizer'),
                                            ('Dessert', 'Dessert'),
                                            ('Beverage', 'Beverage')],
                         validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired(),
                                                           Length(min=1, max=300)])
    price = StringField('Course', validators=[DataRequired(), Length(min=1, max=10)])
    restaurant_id = IntegerField('Restaurant ID', validators=[DataRequired()])
    submit = SubmitField('Submit')

    def validate_name(self, name, restaurant_id):
        name = MenuItem.query.filter_by(name=name, restaurant_id=restaurant_id).first()
        if name:
            raise ValidationError('That item is already on the menu.')


class DeleteConfirmForm(FlaskForm):
    confirm = RadioField('Confirm',
                         choices=[('Delete', 'Delete'),
                                  ('Cancel', 'Cancel')],
                         validators=[DataRequired()])
    submit = SubmitField('Submit')

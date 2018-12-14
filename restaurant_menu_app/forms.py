from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, SubmitField, SelectField,
                     ValidationError, IntegerField, RadioField)
from restaurant_menu_app.models import Restaurant, MenuItem
from wtforms.validators import DataRequired, Length


class RestaurantForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=50)])
    privacy = SelectField('Privacy', choices=[('True', 'Private'),
                                              ('False', 'Public')],
                          validators=[DataRequired()])
    submit = SubmitField('Submit')


class MenuItemsForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=50)])
    course = SelectField('Course', choices=[('Entree', 'Entree'),
                                            ('Appetizer', 'Appetizer'),
                                            ('Dessert', 'Dessert'),
                                            ('Beverage', 'Beverage')],
                         validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired(),
                                                           Length(min=1, max=300)])
    price = StringField('Price', validators=[DataRequired(), Length(min=1, max=10)])
    restaurant_id = IntegerField('Restaurant ID', validators=[DataRequired()])
    submit = SubmitField('Submit')


class DeleteConfirmForm(FlaskForm):
    confirm = RadioField('Confirm',
                         choices=[('Delete', 'Delete'),
                                  ('Cancel', 'Cancel')],
                         validators=[DataRequired()])
    submit = SubmitField('Submit')


class EditItemForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=50)])
    course = SelectField('Course', choices=[('Entree', 'Entree'),
                                            ('Appetizer', 'Appetizer'),
                                            ('Dessert', 'Dessert'),
                                            ('Beverage', 'Beverage')],
                         validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired(),
                                                           Length(min=1, max=300)])
    price = StringField('Price', validators=[DataRequired(), Length(min=1, max=10)])
    restaurant_id = IntegerField('Restaurant ID', validators=[DataRequired()])
    submit = SubmitField('Submit')

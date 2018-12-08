from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length


class RestaurantForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=50)])
    submit = SubmitField('Submit')


class MenuItemsForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=50)])
    course = SelectField('Course', choices=[('Entree', 'Entree'),
                                            ('Appetizer', 'Appetizer'),
                                            ('Dessert', 'Dessert'),
                                            ('Beverage', 'Beverage')],
                         validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired(), Length(min=1, max=300)])
    price = StringField('Course', validators=[DataRequired(), Length(min=1, max=10)])
    submit = SubmitField('Submit')

from flask_wtf import FlaskForm
from wtforms import BooleanField, FloatField, IntegerField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, NumberRange

class AddProductForm(FlaskForm):
    """Form for signing up a new product."""
    name = StringField('Enter the product name:', validators=[DataRequired(message='A name must be provided')])
    description = TextAreaField('Enter the product description: ', validators=[DataRequired(message='A description must be provided')])
    stock = IntegerField('Enter the product actual stock:', validators=[NumberRange(min=0, message='The stock must be positive')], default=0)
    price = FloatField('Enter the product price:', validators=[NumberRange(min=0, message='The price must be positive.')], default=0.0)
    submit = SubmitField('Submit')
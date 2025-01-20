from flask_wtf import FlaskForm
from wtforms import BooleanField, FloatField, IntegerField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, NumberRange

class UpdateProductForm(FlaskForm):
    """Form for signing up a new product."""
    price = FloatField('Enter the new product price:', validators=[NumberRange(min=0, message='The price must be positive.')], default=0.0)
    is_active = SubmitField('Disable product')
    submit = SubmitField('Submit')
    cancel = SubmitField('Cancel')
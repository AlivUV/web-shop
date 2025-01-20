from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo

class SignupForm(FlaskForm):
    """Form for signing up a new user."""
    name = StringField('Enter your name: ', validators=[DataRequired()])
    email = StringField('Enter your email: ', validators=[DataRequired()])
    password = PasswordField('Enter your new password: ', validators=[DataRequired(), EqualTo('confirm_password', message='Passwords must match')])
    confirm_password = PasswordField('Repeat your password: ', validators=[DataRequired()])
    submit = SubmitField('Submit')
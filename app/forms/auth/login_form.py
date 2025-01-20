from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo

class LoginForm(FlaskForm):
    """Form for signing up a new user."""
    email = StringField('Enter your email: ', validators=[DataRequired()])
    password = PasswordField('Enter your passord: ', validators=[DataRequired()])
    submit = SubmitField('Submit')
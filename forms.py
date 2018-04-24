from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(FlaskForm):
	"""docstring for SignupForm"""
	first_name = StringField('First Name', validators=[DataRequired("Please enter your first name.")])
	last_name = StringField('Last Name', validators=[DataRequired("Please enter your last name.")])
	email = StringField('Email', validators=[DataRequired("Please enter your e-mail address."), Email("Please enter a valid e-mail address")])
	password = PasswordField('Password', validators=[DataRequired("Please enter a password."), Length(min=6, message="Passwords must be 6 characters or longer.")])
	submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
	"""Form for signing into the application"""
	email = StringField('Email', validators=[DataRequired("Please enter your e-maill address."), Email("Please enter a valid e-mail address")])
	password = PasswordField('Password', validators=[DataRequired("Please enter your password.")])
	submit = SubmitField('Sign in')

	
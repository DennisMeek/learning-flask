from flask_sqlalchemy import SQLAlchemy  # Import sql alchemy class
from werkzeug import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
	"""docstring for User"""
	__tablename__ = 'users'
	uid = db.Column(db.Integer, primary_key=True)
	firstname = db.Column(db.String(100))
	lastname = db.Column(db.String(100))
	email = db.Column(db.String(120), unique=True)
	pwdhash = db.Column(db.String(54))

	def __init__(self, firstname, lastname, email, password):
		"""Constructor to set each of these class attributes"""
		self.firstname = firstname.title() # forces proper captialization for consistency
		self.lastname = lastname.title()
		self.email = email.lower()
		self.set_password(password) # Encryption hash

	def set_password(self, password):
		"""Function to encrypt the users password"""
		self.pwdhash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.pwdhash, password)

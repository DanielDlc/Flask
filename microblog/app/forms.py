from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, email, EqualTo
import sqlalchemy as sa
from app import db
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Usename', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat password', validators=[DataRequired(), EqualTo('password')]) 
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = db.session.scalar(sa.select(user).where(
            User.username == username.data))
        if User is not None:
            raise ValidationError('Please user a different username.')
        
    def validate_email(self, amail):
        user = db.session.scalar(sa.select(user).where(
            User.email == email.data))
        if User is not None:
            raise ValidationError('Please use a different email adress.')
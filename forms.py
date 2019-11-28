from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError


class LoginForm(FlaskForm):
    
    email = StringField('Email', validators=[DataRequired(), Email(message="Invalid Email")])
    
    password = PasswordField('Password', validators=[DataRequired() ])
    #captcha
    remember  = BooleanField('Remember Me')
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    
    email = StringField('Email', validators=[DataRequired(), Email(message="Invalid Email")])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('confirm password', validators=[DataRequired(), EqualTo('password', message="Passwords do not match, re-enter")] )
    #captcha
    admin_password = PasswordField('admin password', validators=[DataRequired()])
    submit = SubmitField('Register')

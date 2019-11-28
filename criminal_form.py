from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField, BooleanField, DateField, RadioField
from wtforms import validators, ValidationError


class criminal_form(FlaskForm):
    first = StringField(
        "First Name", [validators.required("Please ENter your name")])
    last = StringField("Last Name", [validators.required("please enter name")])
    gender = RadioField('Gender', choices=[('M', 'male'), ('F', "Female")])
    address = StringField("Address")
    cadhar=     IntegerField('Enter the adhar number')
    sub4 = SubmitField("Add criminal")
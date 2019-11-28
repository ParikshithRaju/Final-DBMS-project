# Nothing to do

from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField, BooleanField, DateField, RadioField
from wtforms import validators, ValidationError
from wtforms.fields.html5 import DateField


class crime_form(FlaskForm):
    location = StringField(
        "Address", [validators.required('Enter Crime Address')])
    date = DateField('Enter date',format='%Y-%m-%d')
    department = StringField("Enter Department")
    crime_type = StringField('Enter crime type')
    sub2 = SubmitField("Add Crime")

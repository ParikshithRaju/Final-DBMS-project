# Nothing to do

from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.fields.html5 import DateField


class vform(FlaskForm):
    location = StringField('Enter crime location:')
    start_date = DateField('Start Date', format='%Y-%m-%d')
    end_date = DateField('End Date', format='%Y-%m-%d')
    dept = StringField('Enter Department')
    Id = StringField('Enter crime id')
    Type = StringField('Enter crime type')
    sub3 = SubmitField('genrate')

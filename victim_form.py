# Nothing to do

from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField, BooleanField, DateField, RadioField, SelectField
from wtforms import validators, ValidationError


class victim_form(FlaskForm):
    first = StringField(
        "First Name", [validators.required("Please Enter your name")])
    last = StringField("Last Name", [validators.required("please enter name")])
    gender = SelectField('Gender', choices=[('M', 'male'), ('F', "Female")])
    address = StringField("Address")
    adhar_number = IntegerField('Enter the adhar number')
    sub1 = SubmitField("Add victim")
    
    # def Victim_check(self,aadhar):
    #     #victim_obj = Victim.query.filter_by(aadhar=aadhar.data).first()
    #     # mobile_repeated = Victim.query.filter_by(mobile = _mobile).first()
        
    #     if victim_obj:
    #         raise ValidationError("Aadhar exists!")


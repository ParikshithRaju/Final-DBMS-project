from __main__ import db, login_manager
from wtforms import ValidationError
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# arrested = db.Table('arrested',
#     db.Column('department_id', db.String(10), db.ForeignKey('department.pincode')),
#     db.Column('criminal_id', db.String(10), db.ForeignKey('criminal.aadhar')),
#     db.PrimaryKeyConstraint('department_id', 'criminal_id')
# ) 

# crime = db.Table('crime',
#     db.Column('criminal_id', db.String(10), db.ForeignKey('criminal.aadhar')),
#     db.Column('victim_id', db.String(10), db.ForeignKey('victim.aadhar')),
#     db.Column('Crime type and Description', db.Text),
#     db.Column('Date of Crime', db.Date),
#     db.PrimaryKeyConstraint('victim_id', 'criminal_id')
# )

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=True)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.email}')"

# class PoliceDepartment(db.Model):
#     __tablename__ = "department"
#     pincode = db.Column(db.String(10), primary_key=True, autoincrement=False)
#     location = db.Column(db.String(100), nullable=False)
#     constables = db.Column(db.Integer, nullable = False)
#     inspector = db.Column(db.String(20), unique=True, nullable=False)
#     landline = db.Column(db.String(10), unique=True, nullable=False) #

#     def __repr__(self):
#         return f"User('{self.location}, {self.inspector}, {self.phone_number}')"


# class Criminal(db.Model):
#     __tablename__ = 'criminal'
#     aadhar = db.Column(db.String(10), primary_key=True, autoincrement=False)
#     first_name = db.Column(db.String(10), nullable=False)
#     last_name = db.Column(db.String(10), nullable=False)
#     gender = db.Column(db.String(10), nullable=False)
#     date_of_birth = db.Column(db.Date, nullable=False)
#     address = db.Column(db.String(100), nullable=False)
#     phone_number = db.Column(db.String(10), unique=True, nullable=False)
 
#     def __repr__(self):
#         return f"User('{self.aadhar}, {self.first_name}, {self.last_name}, {self.gender}, {self.address}, {self.date_of_birth}, {self.phone_number}')"


# class Victim(db.Model):
#     __tablename__ = 'victim'
#     aadhar = db.Column(db.String(10), primary_key=True, autoincrement=False)
#     first_name = db.Column(db.String(10), nullable=False)
#     last_name = db.Column(db.String(10), nullable=False)
#     gender = db.Column(db.String(10), nullable=False)
#     date_of_birth = db.Column(db.Date, nullable=False)
#     address = db.Column(db.String(100), nullable=False)
#     mobile = db.Column(db.String(10), unique=True, nullable=False)
#     criminals = db.relationship('Criminal', secondary = crime, backref=db.backref('hurted', lazy='dynamic'))
#     #photo = 

#     def __repr__(self):
#         return f"User('{self.aadhar}, {self.first_name}, {self.last_name}, {self.gender}, {self.address}, {self.date_of_birth}, {self.mobile}')"

    # def validation(self):
    #     if self.query.checkConstraint(len(self.aadhar.data)!=10):
    #         raise  ValidationError("Enter 10 digit adhar number\n")

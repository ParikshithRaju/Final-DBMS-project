from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)   #
app.config['SECRET_KEY'] = '38c14e2f56388ad14ed381557e994a3c'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://testuser:Nikhil1999@@localhost/crimecontrol"

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


from crimecontrol import routes
from flask import Flask, render_template, request, flash, redirect, url_for
from crime_form import crime_form
from victim_form import victim_form
from adddata import addcrime, addvictim, getview, addcriminal
from viewform import vform
from criminal_form import criminal_form
from forms import LoginForm, RegisterForm
from flask_sqlalchemy import SQLAlchemy
import webbrowser
brow=webbrowser.get('firefox')
brow.open_new('http://127.0.0.1:5000')
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_user, logout_user, current_user, login_required

app = Flask(__name__)
app.config['SECRET_KEY'] = '38c14e2f56388ad14ed381557e994a3c'   #pari
app.config['image_uploads_victims']='/home/parikshith/Documents/practice_projects/dbms_draft1/static/victims'
app.config['image_uploads_criminals']='/home/parikshith/Documents/practice_projects/dbms_draft1/static/criminals'
app.config['SQLALCHEMY_DATABASE_URI']="mysql+pymysql://parikshith:wasupmynigga@localhost/practice"

db = SQLAlchemy(app)


bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from models import User


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',title = 'home')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    _form = LoginForm()
    if _form.validate_on_submit():
        user_obj = User.query.filter_by(email = _form.email.data).first()
        # here (above) retrieve the email that's been entered by user while logging in...
        _password = _form.password.data
        if user_obj and bcrypt.check_password_hash(user_obj.password, _password):
            login_user(user_obj, remember=False)
            # next_page = request.args.get('next')
            # if next:
            #     return redirect(next_page)
            # else:
            flash('Login Successful!', 'success')
            return redirect(url_for('home'))
            # or return redirect(next_page) if next else return redirect(url_for('home'))
         # else:
    #if ( not (user_obj ) or not (bcrypt.check_password_hash(user_obj.password, _password)) ):
            flash("Username or password is incorrect",'danger')
    return render_template('login.html', title='Login', form = _form)



@app.route('/register', methods=['POST', 'GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    _form = RegisterForm()
    if _form.validate_on_submit():

        admin_pass = bcrypt.generate_password_hash("admin12345")
        admin = bcrypt.check_password_hash(admin_pass , _form.admin_password.data) #admin12345 is passwd
        new_reg = User.query.filter_by(email = _form.email.data).first()
        # here (above) retrieve the email that's been entered by user while logging in...

        
        if not admin:
            flash("Admin Password is incorrect!",'danger')
            return render_template('register.html', title='Register', form = _form)
            # flash(f'Admin passsword is Incorrect!')

        if new_reg:
            flash("Email taken!",'danger')
            return render_template('register.html', title='Register', form = _form)
        
        if len(_form.email.data) > 50:
            flash("Too many char in email",'danger')
            return render_template('register.html', title='Register', form = _form)
        

        hashed_password = bcrypt.generate_password_hash(_form.password.data).decode('utf-8')
        user = User(email = _form.email.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        # here add the new user to database...
        flash("Registered successfully, Login now!", 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form = _form)


@app.route('/manage', methods=['GET', 'POST'])
@login_required
def crimeenter():
    c = crime_form()
    if request.method == 'POST':
        if c.is_submitted() == False:
            flash("All feilds are required")
            return render_template('crime_form.html', crime_form=c, title='Enter Crime')
        else:
            res1 = request.form
            print(res1)
            a = addcrime()
            a.addcr(res1)
            return(redirect(url_for('addvic')))
    elif request.method == 'GET':
        return render_template('crime_form.html', crime_form=c, title = 'Enter Crime')


@app.route('/addvictim', methods=['GET', 'POST'])
@login_required
def addvic():
    v = victim_form()
    if request.method == 'POST':
        if v.is_submitted() == False:
            return render_template('victim_form.html', victim_form=v, title='Enter Crime')
        else:
            res2 = request.form
            b = addvictim()
            file=request.files['u_img'] 
            file.save(os.path.join(app.config['image_uploads_victims'],file.filename.replace(' ','_')))
            print(res2)
            b.addvi(res2,file.filename)
            return redirect(url_for('crim'))
    elif request.method == 'GET':
        return render_template('victim_form.html', victim_form=v, title = 'Add Victim')


@app.route('/addcriminal',methods=['GET','POST'])
@login_required
def crim():
    c = criminal_form()
    if request.method == 'POST':
        if c.is_submitted() == False:
            return render_template('criminal_form.html', criminal_form=c, title='Enter Crime')
        else:
            res3 = request.form
            b = addcriminal()
            file=request.files['c_img'] 
            file.save(os.path.join(app.config['image_uploads_criminals'],file.filename.replace(' ','_')))
            b.addcrim(res3,file.filename)
            return render_template('choice.html')
    elif request.method == 'GET':
        return render_template('criminal_form.html', criminal_form=c, title = 'Add Criminal') 


@app.route('/view', methods=['GET', 'POST'])
@login_required
def view():
    v = vform()
    if request.method == 'POST':
        res = request.form
        for key, val in res.items():
            print(key, val)
        r = getview()
        result,victims,criminals = r.get(res=res)
        return render_template('output.html', r=result,v=victims,c=criminals, title='Enter Crime')
    elif request.method == 'GET':
        return render_template('view.html', form=v, title = 'View Crime')


@app.route('/aboutus')
def about():
    return render_template('about.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)

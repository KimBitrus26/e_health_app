from flask import request,render_template, redirect, flash, url_for
from app import app
from app.forms import UserLoginForm, MedForm, PractitionerLoginForm, PractitionerRegisterationForm, UserRegisterationForm
from flask_login import LoginManager, UserMixin, login_required, logout_user, current_user, login_user
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import User, Practitioner, Patients
from datetime import datetime
from app import db

#index endpoit
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/malaria")
def malaria():
    results = Patients.query.filter_by(ailment="Malaria").all()
    return render_template("malaria.html", results=results)

@app.route("/ebola")
def ebola():
    results = Patients.query.filter_by(ailment="Ebola").all()
    return render_template("ebola.html", results=results)


@app.route("/covid19")
def covid19():
    results = Patients.query.filter_by(ailment="Covid19").all()
    return render_template("covid.html", results=results)


@app.route("/record")
def record():
    records = User.query.all()
    return render_template("record.html", records=records)
#the login endpoint
@app.route("/login_user", methods=["GET", "POST"])
def user_login():
    form = UserLoginForm(request.form)
    if request.method == "POST":
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember_me.data)
                flash("Successfully logged in", "success")
                # return to attemted protected routes after successfully logged in
                return redirect(url_for('index'))
            flash("Invalid email or password", "info")
            return render_template("login_user.html", form=form)
        flash("Invalid email or password", "danger")
        return render_template("login_user.html", form=form)
    return render_template("login_user.html", form=form)    

#the register endpoint
@app.route("/sign_up_user", methods=["GET", "POST"])
def sign_up_user():
    form = UserRegisterationForm(request.form)
    if request.method == "POST":
        #create an object and pass the hashed password
        hashed_password = generate_password_hash(form.password.data, method="sha256")
        data = User.query.filter_by(email=form.email.data).first()
        if data:
            #check if email alredy in the database
            if data.email == form.email.data:
                flash("User already exist", "danger")
                return render_template("user_register.html", form=form)
        user = User(first_name=form.first_name.data,last_name=form.last_name.data, age=form.age.data, genotype=form.genotype.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash("Successfully registered ", "success")
        return redirect(url_for("user_login"))
        
    return render_template("user_register.html", form=form)

#the login endpoint for practioner
@app.route("/login_practitioner", methods=["GET", "POST"])
def login_practitioner():
    form = PractitionerLoginForm()
    if request.method == "POST":
        result = Practitioner.query.filter_by(email=form.email.data).first()
        if result:
            if check_password_hash(result.password, form.password.data):
                login_user(result, remember=form.remember_me.data)
                # return to attemted protected routes after successfully logged in
                next_page = request.args.get("next")
                return redirect(next_page or url_for('index'))
            flash("Invalid email or password", "info")
            return render_template("login_practioner.html", form=form)
        flash("Invalid email or password", "danger")
        return render_template("login_practitioner.html", form=form)
    return render_template("login_practitioner.html", form=form)    


#the register endpoint for practitioners
@app.route("/sign_up_practitioner", methods=["GET", "POST"])
def sign_up_practitioner():
    form = PractitionerRegisterationForm(request.form)
    if request.method == "POST":
        #create an object and pass the hashed password
        hashed_password = generate_password_hash(form.password.data, method="sha256")
        data = Practitioner.query.filter_by(email=form.email.data).first()
        if data:
            #check if email alredy in the database
            if data.email == form.email.data:
                flash("User already exist", "danger")
                return render_template("practitioner_register.html", form=form)
        practitioner = Practitioner(first_name=form.first_name.data,last_name=form.last_name.data,email=form.email.data,expertise=form.expertise.data,password=hashed_password)
        db.session.add(practitioner)
        db.session.commit()
        flash("Successfully registered ", "success")
        return redirect(url_for("login_practitioner"))
        
    return render_template("practitioner_register.html", form=form)

@app.route("/med", methods=["GET", "POST"])
def med():
    form = MedForm(request.form)
    if request.method == "POST":
        patients = Patients(full_name=form.full_name.data, date_of_birth=form.date_of_birth.data, gender=form.gender.data,genotype=form.genotype.data, ailment=form.ailment.data)
        db.session.add(patients)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('med_form.html', form=form)

@app.route("/chart")
def chart():
    legend = 'E-Health Data'
    #labels = ["Ebola", "Covid19", "Malaria"]
    labs = Patients.query.all()
    
    values = [10, 4, 8]
    return render_template('chart.html', labs=labs, values=values, legend=legend)
 
 

#dashboard endpoint
@app.route("/dashboard")
#@login_required
def dashboard():
    return render_template("dashboard.html")

#logging out endpoint
@app.route('/logout')
#@login_required
def logout():
    logout_user()
    flash('You are now logged out', "success")
    return redirect(url_for('index'))

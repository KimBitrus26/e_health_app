from flask_wtf import Form
from wtforms import StringField, RadioField, SelectField, BooleanField, TextAreaField,PasswordField, DateField, validators, SubmitField, ValidationError


#user form
class UserRegisterationForm(Form):
    first_name = StringField(u'First name', validators=[validators.input_required()])
    last_name = StringField(u'Last name', validators=[validators.input_required()])
    age = StringField(u'age', validators=[validators.input_required()])
    genotype = StringField(u'Genotype', validators=[validators.input_required()])
    email = StringField(u'Email', validators=[validators.input_required(), validators.Email()])
    password = PasswordField('Password', [validators.DataRequired(), validators.EqualTo('confirm', message='password do not match')])
    confirm = PasswordField('Confirm password')

class PractionerRegisterationForm(Form):
    first_name = StringField(u'First name', validators=[validators.input_required()])
    last_name = StringField(u'Last name', validators=[validators.input_required()])
    email = StringField(u'Email', validators=[validators.input_required(), validators.Email()])
    expertise = StringField(u'Expertise', validators=[validators.input_required()])
    password = PasswordField('Password', [validators.DataRequired(), validators.EqualTo('confirm', message='password do not match')])
    confirm = PasswordField('Confirm password')

#login form
class UserLoginForm(Form):
    email = StringField('Email', validators=[validators.input_required(), validators.Email()])
    password = PasswordField('Password', [validators.DataRequired()])
    remember_me = BooleanField('Keep me logged in')
class PractionerLoginForm(Form):
    email = StringField('Email', validators=[validators.input_required(), validators.Email()])
    password = PasswordField('Password', [validators.DataRequired()])
    remember_me = BooleanField('Keep me logged in')

#posting form
class MedForm(Form):
    full_name = StringField(u'Full name', validators=[validators.input_required()])
    date_of_birth = DateField(u'age', validators=[validators.input_required()])
    gender = SelectField(u'Gender', choices=[('female','female'), ('male','male')] ,validators=[validators.input_required()])
    genotype = StringField(u'Genotype', validators=[validators.input_required()])
    ailment = SelectField(
        'Ailment',
        choices=[('Ebola', 'Ebola'), ('Covid19','Covid19'), ('Malaria', 'Malaria')]
    )


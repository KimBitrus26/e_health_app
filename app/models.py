from flask_login import  UserMixin
from app import db
from app import login
from app import app


#user model
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.String(100), nullable=False)
    genotype = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(300), nullable=False) 

    #constructor
    def __init__(self, first_name, last_name, age, genotype, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age 
        self.genotype = genotype
        self.email = email  
        self.password = password  


    # a callback function that loads a user
    # @login.user_loader
    # def load_user(id):
    #     return User.query.get(id)

    @login.user_loader
    def load_user(id):
        return User.query.get(int(id))


#practioner model
class Practioner(UserMixin, db.Model):
    __tablename__ = 'practioners'
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(100))
    expertise = db.Column(db.String(100))
    password = db.Column(db.String(300)) 
    
    # #constructor
    def __init__(self, first_name, last_name, email, expertise, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.expertise = expertise
        self.password = password

class Patients(db.Model):
    __tablename__ = 'patients'
    id = db.Column(db.Integer, primary_key = True)
    full_name = db.Column(db.String(30), nullable=False)
    date_of_birth = db.Column(db.DateTime)
    gender = db.Column(db.String(30), nullable=False)
    genotype = db.Column(db.String(5), nullable=False)
    ailment = db.Column(db.String(100), nullable=False) 

    def __init__(self, full_name, date_of_birth, gender, genotype, ailment):
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.genotype = genotype
        self.ailment = ailment
    
                  
#programmatic creating database
db.create_all()

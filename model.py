import os
from flask import Flask
from sqlalchemy import Table, Column, Integer, ForeignKey, Numeric
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship


project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "Data.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(app)
###############################################################################################
###############################################################################################
class Accounts(db.Model):
    rowid       = db.Column(db.Integer, nullable=False, primary_key=True)
    name        = db.Column(db.String(80), nullable=False)
    email       = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(80), nullable=False)
    phonenumber = db.Column(db.String(80), unique=True, nullable=False)
    address     = db.Column(db.String(80), unique=True, nullable=False)

    @property
    def password(self):
        raise AttributeError("password is not a readable attribute.")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


    #def __repr__(self):
		#return "({}, {}, {}, {})".format(self.rowid, self.name, self.login, self.password)
###############################################################################################
###############################################################################################
class Delivery(db.Model):
    rowid       = db.Column(db.Integer, nullable=False, primary_key=True)
    product     = db.Column(db.String(80), nullable=False)
    time        = db.Column(db.String(80), nullable=False)
    date        = db.Column(db.String(80), nullable=False)
    status      = db.Column(db.Boolean, nullable=False)
    buyerID     = db.Column(db.DateTime, nullable=False)

    #def __repr__(self):
		#return "({}, {}, {}, {})".format(self.rowid, self.name, self.login, self.password)
###############################################################################################
###############################################################################################
class Product(db.Model):
    rowid       = db.Column(db.Integer, nullable=False, primary_key=True)
    product     = db.Column(db.String(80), nullable=False)
    available   = db.Column(db.String(80), unique=True, nullable=False)
    color       = db.Column(db.String(80), nullable=False)
    size        = db.Column(db.Boolean, nullable=False)
    
    #def __repr__(self):
		#return "({}, {}, {}, {})".format(self.rowid, self.name, self.login, self.password)
###############################################################################################
###############################################################################################
class Money(db.Model):
    rowid       = db.Column(db.Integer, nullable=False, primary_key=True)
    revenue     = db.Column(db.Integer, nullable=False)
    spenditure  = db.Column(db.Integer, nullable=False)

class EmployeeAccounts(db.Model):
    rowid       = db.Column(db.Integer, nullable=False, primary_key=True)
    name        = db.Column(db.String(80), nullable=False)
    email       = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(80), nullable=False)
    phonenumber = db.Column(db.String(80), unique=True, nullable=False)
    address     = db.Column(db.String(80), unique=True, nullable=False)

    @property
    def password(self):
        raise AttributeError("password is not a readable attribute.")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    
    def update_password(self, old_password, new_password):
        if self.verify_password(old_password):
            self.password=new_password
            return True
        return False
      

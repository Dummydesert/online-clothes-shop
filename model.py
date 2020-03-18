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
    password    = db.Column(db.String(80), nullable=False)
    created     = db.Column(db.DateTime, nullable=False)
    updated     = db.Column(db.DateTime, nullable=False)
    phonenumber = db.Column(db.String(80), unique=True, nullable=False)
    address     = db.Column(db.String(80), unique=True, nullable=False)

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
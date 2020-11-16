from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from website.config import Config


app=Flask(__name__)
app.config.from_object(Config)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:19970613@localhost:3306/testtable'
db=SQLAlchemy(app)
login_manager=LoginManager(app)
login_manager.init_app(app)
login_manager.login_view='login'

#!!!!
from website import form
from website import routes
from website import register



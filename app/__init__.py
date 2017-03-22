from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = "wellth1s$ho^lb@ super #4m1$$3d key101l"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://comp3180:comp@localhost/project1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

db = SQLAlchemy(app)


app.config.from_object(__name__)
from app import views
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os

db_location = os.getcwd
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

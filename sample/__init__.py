from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://kwood:@localhost/python-sample'
db = SQLAlchemy(app)

import sample.views

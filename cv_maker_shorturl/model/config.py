from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# config your postgresql DB
POSTGRES = {
    'user': 'postgres',
    'pw': '2410',
    'db': 'login',
    'host': '0.0.0.0',
    'port': '5432',
}

# config your link and content activate of reset password
SHORT_LINK = "http://localhost:5000/{}"

# create app and setup config for your app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

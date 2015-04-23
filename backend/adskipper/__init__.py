import config

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object(config)

# Create database connection object
db = SQLAlchemy(app)

import adskipper.views
# import adskipper.views.api.v1.cinemas
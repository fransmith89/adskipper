import json

from flask import request
from flask import session, url_for, abort, jsonify, g
from adskipper import db, app

@app.route("/")
@app.route("/index")
def index():
    return "hi"


@app.route("/hodor")
def hodor():
    return 'hodor'
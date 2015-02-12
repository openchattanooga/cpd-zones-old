#!/usr/bin/env python
import os
import urllib, urllib2
import json
import random
import geoalchemy2 as geo
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from flask import render_template
from forms import SearchForm

app = Flask(__name__)
app.secret_key = 'some_secret_key'

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

# custom jinja line delimeters
app.jinja_env.line_statement_prefix = '%'
app.jinja_env.line_comment_prefix = '##'

class Zone(db.Model):
    __tablename__ = 'zones'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(length=200), autoincrement=False, nullable=False)
    geog = db.Column(geo.Geography(geometry_type='MULTIPOLYGON', srid='4326'))

class Officer(db.Model):
    __tablename__ = 'officers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(length=200), nullable=False)
    email = db.Column(db.Unicode(length=200), nullable=False)
    phone = db.Column(db.Unicode(length=200), nullable=False)
    title = db.Column(db.Unicode(length=200), nullable=False)

def decode_address_to_coordinates(address):
    params = {
            'address' : address,
            'sensor' : 'false',
    }
    url = 'http://maps.google.com/maps/api/geocode/json?' + urllib.urlencode(params)
    response = urllib2.urlopen(url)
    result = json.load(response)
    try:
            return result['results'][0]['geometry']['location']
    except:
            return None

@app.route("/", methods=['GET', 'POST'])
def index():
    form = SearchForm()
    data = {}
    cordinates = None
    if form.validate_on_submit():
        query = form.query.data
        cordinates = decode_address_to_coordinates(query)
    return render_template('index.html', form=form, cordinates=cordinates)


if __name__ == "__main__":
    manager.run()

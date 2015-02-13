#!/usr/bin/env python
import os
import urllib, urllib2
import json
import random
import geoalchemy2 as geo
from shapely.geometry import asShape
from geoalchemy2.shape import from_shape
import geojson
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
    name = db.Column(db.Unicode(length=200), nullable=False)
    regions = db.relationship("Region")


    def __init__(self, name):
        self.name = name

class Region(db.Model):
    __tablename__ = 'regions'
    id = db.Column(db.Integer, primary_key=True)
    geog = db.Column(geo.Geography(geometry_type='POLYGON', srid='4326'))
    zone_id = db.Column(db.Integer, db.ForeignKey('zones.id'))
    zone = db.relationship("Zone")

    def __init__(self, geog, zone_id):
        self.geog = geog
        self.zone_id = zone_id

class Officer(db.Model):
    __tablename__ = 'officers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(length=200), nullable=False)
    email = db.Column(db.Unicode(length=200), nullable=False)
    phone = db.Column(db.Unicode(length=200), nullable=False)
    title = db.Column(db.Unicode(length=200), nullable=False)

    def __init__(self, name, email, phone, title):
        self.name = name
        self.email = email
        self.phone = phone
        self.title = title

class ZoneAssignment(db.Model):
    __tablename__ = 'zone_assignments'
    id = db.Column(db.Integer, primary_key=True)
    zone_id = db.Column(db.Integer, db.ForeignKey('zones.id'))
    officer_id = db.Column(db.Integer, db.ForeignKey('officers.id'))

    zone = db.relationship(Zone, backref="zone_assignments")
    officer = db.relationship(Officer, backref="zone_assignments")

    def __init__(self, zone_id, officer_id):
        self.zone_id = zone_id
        self.officer_id = officer_id

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

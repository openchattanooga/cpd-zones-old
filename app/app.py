#!/usr/bin/env python
import os
import urllib
import json
import random
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



@app.route("/", methods=['GET', 'POST'])
def index():
    form = SearchForm()
    if form.validate_on_submit():
        query = form.query.data
    # returning an html template
    return render_template('index.html', form=form)


if __name__ == "__main__":
    manager.run()

#!/usr/bin/env python
import urllib,json
import random
from flask import Flask
from flask import render_template
from forms import SearchForm

app = Flask(__name__)
app.secret_key = 'some_secret_key'

@app.route("/")
@app.route("/index")
def index():
	# returning an html template
    return render_template('index.html')





if __name__ == "__main__":
    port=5000
    app.run(host='0.0.0.0', debug=True, port=port)

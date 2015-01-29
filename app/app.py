#!/usr/bin/env python
import urllib,json
import random
from flask import Flask
from flask import render_template
import flask_raptor
from forms import SearchForm

app = Flask(__name__)
app.config['RAPTOR_CHANCE'] = .2
flask_raptor.init_app(app)
app.secret_key = 'some_secret_key'

@app.route("/")
@app.route("/index")
def index():
	# returning an html template
    return render_template('index.html')

@app.route("/python")
def python():
	# returning text
    return "Python all the things!"

@app.route("/flask")
def flask():
	# returning simple html
    return "<h1>Flask all the web!</h1>"

@app.route("/extns")
def extensions():
	# returning a list to a template
	extns = ['Flask', 'Jinja2', 'Flask-SQLAlchemy', 'Flask-Admin', 'Flask-Classy', 'Flask-Raptor']
	return render_template('extensions.html', extns=extns)

@app.route("/gifs", methods=['GET', 'POST'])
def gifs():
	# sending form and gif to template
	# validating form on submit, querying giphy, sending to template
	form = SearchForm()
	if form.validate_on_submit():
		query = form.query.data
		gif = get_image(query)
		return render_template('gifs.html', gif=gif, form=form)

	gif = 'static/img/dwight.gif'
	return render_template('gifs.html', gif=gif, form=form)


def get_image(query):
	# querying giphy api
	url = 'http://api.giphy.com/v1/gifs/search?q='
	api_key = 'dc6zaTOxFJmzC&limit=5'
	data = json.loads(urllib.urlopen(url+query+'&api_key='+api_key).read())
	item = random.choice(data['data'])
	gif = item['images']['original']['url']
	return gif


if __name__ == "__main__":
    port=5000
    app.run(host='0.0.0.0', debug=True, port=port)
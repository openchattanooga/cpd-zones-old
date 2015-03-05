# CPD Zones Flask App

This application is meant to help Chattanoogans find which CPD zone they live in.

Type in your address in the application and it will display:

  * The CPD zone you live in
  * The CPD Captain that is assigned to your zone.
  * The CPD Lieutenant that is assigned to your zone.
  * The contact information (e-mail, phone) for the CPD Captain and Lieutenant so that they can be contacted for non-emergencies.

## Requirements

- [Python 2.7](https://www.python.org/)
- [Virtualenv](https://virtualenv.pypa.io/en/latest/)
- [Pip](https://pip.pypa.io/en/latest/installing.html)
- [Postgres](http://www.postgresql.org/)
- [PostGIS](http://postgis.net/)

## Installation

~~~ sh
# Clone repo and cd to repo
git clone git@github.com:openchattanooga/cpd-zones.git cpd-zones && cd cpd-zones

# Create virtual environment
virtualenv env

# Activate virtual environment
. env/bin/activate

# Install project dependencies
pip install -r requirements.txt

# Run migrations
DATABASE_URL=postgres://myusername:mypassword@localhost/mydatabase python app.py db upgrade

# Load Data (also flushes database)
DATABASE_URL=postgres://myusername:mypassword@localhost/mydatabase python app.py reset_data

# Run project
DATABASE_URL=postgres://myusername:mypassword@localhost/mydatabase python app.py runserver

# Open web browser to localhost:5000
open http://localhost:5000
~~~

## Contribute

- [Issue Tracker](github.com/openchattanooga/cpd-zones/issues)
- [Source Code](github.com/openchattanooga/cpd-zones)

## Support

If you are having issues, please let us know!


## License

The project is licensed under the MIT license. See `LICENSE.md` for more details."


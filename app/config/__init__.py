# -*- coding: utf-8 -*-

import os
import config

"""Set up config variables.

If environment variable APP_SETTINGS is set to dev and the config/dev.py
file exists then use that file as config settings, otherwise pull in settings from the production environment

Add the following to your .bashrc/.zshrc file for local development.
export APP_SETTINGS="dev"
"""

if os.environ.get('APP_SETTINGS') == 'dev':
    try:
        import dev as config  # config/dev.py
    except:
        print "Please create config/dev.py"
else:
    # production server environment variables
    config.DATABASE_URL = os.environ.get('DATABASE_URL')
    config.SECRET_KEY = os.environ.get('SECRET_KEY')
    config.DEBUG = False
    config.RELOAD = False

try:
    any([config.DATABASE_URL, config.SECRET_KEY, config.DEBUG, config.RELOAD]) is None
except Exception, e:
    missing_var = e.message.split()[-1]
    print 'A config variable has not been set:', missing_var
    print 'This variable can be set in dev.py if in development\n' \
          'or as an environment variable on production.'
    raise ValueError(e)
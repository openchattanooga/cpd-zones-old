# -*- coding: utf-8 -*-

import os
basedir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), os.pardir))

DATABASE_URL = 'postgresql:///cpd-zones'
SECRET_KEY = 'awesome_sauce'
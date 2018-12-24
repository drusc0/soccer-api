import os 
from token import TOKENS

basedir = os.path.abspath( os.path.dirname( __file__ ) )


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = ""
    FUTBOL_DATA_TOKEN = TOKENS['futbol_key']

class ProductionConfig( Config ):
    DEBUG = False

class DevelopmentConfig( Config ):
    DEBUG = True
    TESTING = True

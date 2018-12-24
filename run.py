from flask import Flask, Blueprint
from flask_restful import Api
from app import api_bp
import os


def create_app():
    # api creation
    app = Flask(__name__)
    app.config.from_object( os.environ['APP_SETTINGS'] )
    # register blueprint
    app.register_blueprint( api_bp, url_prefix='/api' )
    return app

if __name__ == '__main__':
    app = create_app()
    app.run()
    print( "Environment: {}".format( os.environ['APP_SETTINGS'] ) )

import os
from flask import Flask, Blueprint, render_template
from flask_restful import Resource, Api

api_bp = Blueprint( 'api', __name__)
api = Api(api_bp)


#Routes
class IndexResource( Resource ):
    def get( self ):
        return render_template( 'index.html' )
api.add_resource( IndexResource, '/index' )
#@app.route('/', methods=['GET'])
#def index():
#    return render_template('index.html')



#@app.route('/hello')
#def hello():
#    return "Hello World!"
#
#
#
#@app.route( '/<name>')
#def hello_name(name):
#    return "Hello {}!".format(name)
#
#
#
#if __name__ == '__main__':
#    app.run()
#    print(os.environ['APP_SETTINGS'])

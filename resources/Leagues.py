from flask_restful import Resource
from services import Service

class LeaguesResource( Resource, Service ):
    def get( self ):
        return 

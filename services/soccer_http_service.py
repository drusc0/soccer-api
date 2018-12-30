import http.client
import json
import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from config import Config

class Service( object ):
    _url = None
    _headers = None

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers
        self.connection = http.client.HTTPConnection( self._url )

    def get(self, endpoint):
        return self.connection.request('GET',
                endpoint,
                None,
                self._headers)

    @property 
    def url(self):
        return self._url

    @url.setter
    def url( self, url ):
        # TODO: add some connection testing code
        self._url = url

    @property
    def headers(self):
        return self._headers

    @headers.setter
    def headers(self, headers):
        self._headers = headers


class SoccerService( Config ):
    _instance = None
    headers = { 'X-Auth-Token': Config.FUTBOL_DATA_TOKEN }
    url = 'api.football-data.org'

    def __init__(self):
        if SoccerService._instance is None:
            print("instance has not been set")
            SoccerService._instance = Service(self.url, self.headers)

        self.__dict__['_SoccerService_instance'] = SoccerService._instance

    def __getattr__(self, attr):
        return getattr(self._instance, attr)

    def __setattr__(self, attr, val):
        return setattr(self._instance, attr, val)

    @staticmethod
    def getInstance():
        SoccerService()
        return SoccerService._instance

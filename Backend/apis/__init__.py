from flask_restful import Api
from .song import SongResource, CheckGuessResource
from .ai import RandomLyric

def init_apis(app):
    api = Api(app, prefix='/api/v1')

    api.add_resource(SongResource, '/song')
    api.add_resource(CheckGuessResource, '/check-guess')

    api.add_resource(RandomLyric, '/random-lyric')

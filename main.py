from flask import Flask
from flask_restful import Resource, Api
from flask import request
from flask_cors import CORS
import firebase_admin

from views.hero import HeroesHandler

# start da  API
app = Flask(__name__)
CORS(app)
API = Api(app)

cred = firebase_admin.credentials.Certificate(
    './tour-of-heroes-15c07-firebase-adminsdk-9riym-31509a37e4.json')

firebase_admin.initialize_app(credential=cred)


@app.before_request
def start_request():
    """Start api request"""
    if request.method == 'OPTIONS':
        return '', 200
    if not request.endpoint:
        return 'Sorry, Nothing at this URL.', 404

#classe principal
class Index(Resource):
    """ class return API index """

    def get(self):
        """return API"""
        return {"API": "Heroes"}


# Nossa primeira url
API.add_resource(Index, '/', endpoint='index')

#rota apontando para a classe de hero da view
API.add_resource(HeroesHandler, '/heroes', endpoint='heroes')

if __name__ == '__main__':

    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]

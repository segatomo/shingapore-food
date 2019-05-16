from flask import Flask, session, request, jsonify, make_response
from flask_restplus import Api, Resource, fields
from flask_cors import CORS
import requests

import json
import sys
import os

# from redis import Redis
# app.config['SESSION_REDIS'] = Redis(host=app.config['REDIS_HOST'], port=app.config['REDIS_PORT'])
# Session(app)


args = sys.argv
env = os.getenv("APP_ENV", "local")

app = Flask(__name__)
app.config.from_pyfile("config/{}.properties".format(env))
api = Api(app, version='0.0.1', title='API', description='API')

app.secret_key = app.config['SECRET_KEY']
app.supports_credentials = True
CORS(app, resources={r"/*": {"origins": "*"}})

ns = api.namespace('api')


@ns.route('/health')
class HealthCheck(Resource):

    @staticmethod
    def get():
        return jsonify({"status": "ok", "message": "this is message from Flask"})

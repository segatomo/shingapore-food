from flask import Flask, session, request, jsonify, make_response
from flask_restplus import Api, Resource, fields
from flask_cors import CORS
import requests

import json
import sys
import os

from app.models.db_connector import DatabaseAccessor
from app.models.users import Users

import os

args = sys.argv
env = os.getenv("APP_ENV", "local")

app = Flask(__name__)
app.config.from_pyfile("config/{}.properties".format(env))
api = Api(app, version='0.0.1', title='API', description='API')

app.secret_key = app.config['SECRET_KEY']
app.supports_credentials = True
CORS(app, resources={r"/*": {"origins": "*"}})

ns = api.namespace('api')

db = DatabaseAccessor.get_session(app.config)


@ns.route('/health')
class HealthCheck(Resource):

    @staticmethod

    def get():
        user = db.query(Users).filter_by(name="wada").first()
        if user:
            print(user.id)
            print(user.name)
            return jsonify(user.serialize)
        else:
            return jsonify({"id": 0, "name": "hogehoge"})

@ns.route('/upload-pictures')
class FileUploader(Resource):

    @staticmethod
    def post():
        print(request.files)

        # file を Vue.js から受け取ります。
        target_file = request.files['picture_data']

        # file を /tmp のフォルダに格納します。
        target_file.save("/tmp/{}".format(target_file.filename))
        # データベースのuser:john.pass:due123さんのところに画像のパスを加える
        print(target_file)
        return jsonify({"status": "ok"})

@ns.route('/login')
class LogIn(Resource):
    @staticmethod
    def post():
        #print('enter')
        data = request.data
        json_data = json.loads(data)
        #print(json_data)
        username=json_data['username']
        password=json_data['password']

        print(username)
        print(password)
        if username!= app.config['USERNAME']:
            #console.log(username)
            return jsonify({"accountinfo":False,"outinfo":"ユーザー名が違います"})
        elif password!=app.config['PASSWORD']:
            #console.log(username)
            return jsonify({"accountinfo":False,"outinfo":"パスワードが違います"})
        elif password!=app.config['PASSWORD'] and username!=app.config['USERNAME']:
            #console.log(username)
            return jsonify({"accountinfo":False,"outinfo":"ユーザー名とパスワードが違います"})
        else :
            #console.log(username)
            return jsonify({"accountinfo":True})


@ns.route('/read-pictures')
class PicturesReader(Resource):

    @staticmethod

    def get():
        user = db.query(Users).filter_by(name="wada").first()
        if user:
            print(user.id)
            print(user.name)
            return jsonify(user.serialize)
        else:
            return jsonify({"id": 0, "name": "hogehoge"})


@ns.route('/save-into-database')
class SaveIntoDatabase(Resource):
    def get():
        user = db.query(Users)

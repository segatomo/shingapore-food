from flask import Flask, session, request, jsonify, make_response, render_template
from flask_restplus import Api, Resource, fields
from flask_cors import CORS
from flask_session import Session
import requests

import json
from urllib.parse import parse_qsl
import sys
import os
import sched
import time
from datetime import datetime
import collections
# from redis import Redis

import hashlib
import hmac
import base64


args = sys.argv
env = os.getenv("APP_ENV", "local")

app = Flask(__name__)
app.config.from_pyfile("config/{}.properties".format(env))
api = Api(app, version='0.0.1', title='API', description='API')

app.secret_key = app.config['SECRET_KEY']
app.config['SESSION_REDIS'] = Redis(host=app.config['REDIS_HOST'], port=app.config['REDIS_PORT'])
app.supports_credentials = True
Session(app)
CORS(app, resources={r"/*": {"origins": "*"}})

ns = api.namespace('api')
pns = api.namespace('')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/health')
def check_health():
    return jsonify({"status": "ok"})

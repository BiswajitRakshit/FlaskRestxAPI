from flask import Flask,jsonify,request
from flask_restx import Api, Resource,fields
from controller import *
from config import config

c = config()

app = Flask(__name__)

api = Api(app)

api.add_resource(DataOparetor, '/operations')

if __name__ == '__main__':
    app.run(debug = c._config__DEBUG)
    
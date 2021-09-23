from flask import Flask,jsonify,request
from flask_restx import Api, Resource,fields
from controller import *

app = Flask(__name__)

api = Api(app)

api.add_resource(DataOparetor, '/test')

if __name__ == '__main__':
    app.run(debug = True)
    
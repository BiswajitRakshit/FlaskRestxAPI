from flask import Flask,jsonify,request
from flask_restx import Api, Resource,fields
from model import *
from helper import *
import json
from json.decoder import JSONDecodeError

def getFunctions(key):
    model = Operations()
    functions = {1: model.fetch, 2: model.fetchById, 3: model.update, 4: model.add, 5: model.delete}
    return functions[key]

class DataOparetor(Resource):
    
    def get(self):
        try:
            dataByUser = request.json
            data = getFunctions(1)()
            if  dataByUser != None:
                ids = dataByUser['id']
                data = getFunctions(2)(ids)
                
            return getCustomResponse(success=True, 
                                     message="Success, The Resource has been fetched and is transmitted in DATA.", 
                                     data=data, status_code=200)
        except Exception as e:
            return getCustomResponse(success=False, 
                                      message=str(e), 
                                      data=None, status_code=400)
    
    def put(self):
        try:
            dataByUser = request.json
            if dataByUser != None: 
                data = getFunctions(3)(dataByUser)
            
            return getCustomResponse(success=True, 
                                     message="OK, Update Request has succeeded.", 
                                     data=data, status_code=201)
        except Exception as e:
            return getCustomResponse(success=False, 
                                     message=str(e), 
                                     data=None, status_code=400)

    def post(self):
        try:
            dataByUser = request.json
            if dataByUser != None:         
                data = getFunctions(4)(dataByUser)
                
            return getCustomResponse(success=True, 
                                     message="Success, The Resource has been added and is transmitted in DATA.", 
                                     data=data, status_code=200)
        except Exception as e:
            return getCustomResponse(success=False, 
                                     message=str(e), 
                                     data=None, status_code=400)
        
    def delete(self):
        try:
            dataByUser =request.json
            
            if dataByUser != None:
                ids = dataByUser['id']
                data = getFunctions(5)(ids) 
            
            return getCustomResponse(success=True, 
                                     message="OK, Delete Request deletes the specified resource.", 
                                     data=data, status_code=200)
        except Exception as e:
            return getCustomResponse(success=False, 
                                     message=str(e), 
                                     data=None, status_code=400)
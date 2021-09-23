from flask import Flask,jsonify,request, jsonify
from flask_restx import Api, Resource,fields
from model import *
import json

model = Operations()

class DataOparetor(Resource):
    def get(self):
        try:
            dataByUser = request.get_json()
            
            if dataByUser != None:
                data = model.fetchById(dataByUser)
            else:
                data = model.fetch()
                
            return jsonify(data)
        
        except:
            return {"Note": "Error"}
        
        
    def put(self):
        try:
            dataByUser = request.get_json()
        
            if dataByUser != None: 
                data = model.update(dataByUser)
            
            return jsonify(data)
            
        except:
            return {"Note" : "Error"}


    def post(self):
        try:
            dataByUser = request.get_json()
            
            if dataByUser != None:         
                data = model.add(dataByUser)
                
            return jsonify(data)
            
        except:
            return {"Note" : "Error"}
        
        
    def delete(self):
        try:
            dataByUser =request.get_json()
            
            data = model.delete(dataByUser) 
            
            
            return jsonify(data)
            
        
        except:
            return {"Note" : "Error"}
        
                
            
            
        
    
    
        

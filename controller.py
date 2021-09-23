from flask import Flask,jsonify,request, jsonify
from flask_restx import Api, Resource,fields
from model import *
from decorator import *
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
                
            return smdResponce(data = data, statusCode=200)
        
        except:
            return smdResponce(data = None, statusCode=400)
        
        
    def put(self):
        try:
            dataByUser = request.get_json()
        
            if dataByUser != None: 
                data = model.update(dataByUser)
            
            return smdResponce(data = data, statusCode=200)
            
        except:
            return smdResponce(data = None, statusCode=400)


    def post(self):
        try:
            dataByUser = request.get_json()
            
            if dataByUser != None:         
                data = model.add(dataByUser)
                
            return smdResponce(data = data, statusCode=200)
            
        except:
            return smdResponce(data = None, statusCode=400)
        
        
    def delete(self):
        try:
            dataByUser =request.get_json()
            
            data = model.delete(dataByUser) 
            
            
            return smdResponce(data = data, statusCode=200)
            
        
        except:
            return smdResponce(data = None, statusCode=400)
        
                
            
            
        
    
    
        

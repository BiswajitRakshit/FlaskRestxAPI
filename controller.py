from flask import Flask,jsonify,request, jsonify
from flask_restx import Api, Resource,fields
from model import *
from helper import *
import json

model = Operations()

class DataOparetor(Resource):
    def get(self):
        try:
            dataByUser = request.get_json()
            
            if dataByUser != None:
                ids = dataByUser['id']
                data = model.fetchById(ids)
                
            else:
                data = model.fetch()
                
            return smdResponce(data = data, method = "get")
        
        except:
            return smdResponce(data = None)
        
        
    def put(self):
        try:
            dataByUser = request.get_json()
        
            if dataByUser != None: 
                data = model.update(dataByUser)
            
            return smdResponce(data = data, method = "put")
            
        except:
            return smdResponce(data = None)


    def post(self):
        try:
            dataByUser = request.get_json()
            
            if dataByUser != None:         
                data = model.add(dataByUser)
                
            return smdResponce(data = data, method = "post")
            
        except:
            return smdResponce(data = None)
        
        
    def delete(self):
        try:
            dataByUser =request.get_json()
            
            if dataByUser != None:
                ids = dataByUser['id']
                data = model.delete(ids) 
            
            
            return smdResponce(data = data, method = "delete")
            
        
        except:
            return smdResponce(data = None)
        
                
            
            
        
    
    
        

from flask import Flask,jsonify,request, jsonify
from flask_restx import Api, Resource,fields
from model import *
from helper import *
import json

model = Operations()

functions = {"1": model.fetch, "2": model.fetchById, "3": model.update, "4": model.add, "5": model.delete}

class DataOparetor(Resource):
    def get(self):
        try:
            
            dataByUser = request.get_json()
            
            if dataByUser != None:
                ids = dataByUser['id']
                count = "2"
                data = functions[count](ids)
                
            else:            
                count = "1"
                data = functions[count]()
                
                
            return smdResponce(data = data, method = "get")
        
        except:
            return smdResponce()
        
        
    def put(self):
        try:
            dataByUser = request.get_json()
        
            if dataByUser != None: 
                count = "3"
                data = functions[count](dataByUser)
            
            return smdResponce(data = data, method = "put")
            
        except:
            return smdResponce()


    def post(self):
        try:
            dataByUser = request.get_json()
            
            if dataByUser != None:         
                count = "4"
                data = functions[count](dataByUser)
                
            return smdResponce(data = data, method = "post")
            
        except:
            return smdResponce()
        
        
    def delete(self):
        try:
            dataByUser =request.get_json()
            
            if dataByUser != None:
                ids = dataByUser['id']
                count = "5"
                data = functions[count](ids) 
            
            
            return smdResponce(data = data, method = "delete")
            
        
        except:
            return smdResponce()
        
                
            
            
        
    
    
        


import json
from flask import jsonify


def getMessage(statusCode):
    
    if statusCode == 400:
        message = "There are misakes..."
    elif statusCode == 200:
        message = "Ok, There is no problems"
    else:
        message = "Error from status Code: " + str(statusCode)
    
    return message


    
def smdResponce(data = None):
    
    starusCode = 500
    
    if data != None:
        
        statusCode = 200
        message = getMessage(statusCode)
        
        
        responce = {
            "data" : data,
            "message" : message,
            "status" : statusCode
            }
        
    else:
        statusCode = 400
        message = getMessage(statusCode)
        
        responce = {
            
            "message" : message,
            "status" : statusCode
            }
    
    return jsonify(responce)





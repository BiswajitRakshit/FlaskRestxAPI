
import json
from flask import jsonify


def getMessage(statusCode, method):
    
    if statusCode == 400:
        message = "400 Bad Request"
        
    elif statusCode == 200:
        if method == 'get':
            message = "The resource has been fetched and is transmitted in DATA."
            
        if method == 'post':
            message = "The resource describing the result of the action is added in DATA."
            
        if method == 'put':
             message = "The Request has succeeded"
             
        if method == 'delete':
            message = "Request method deletes the specified resource"
            
    else:
        message = "Error from status Code: " + str(statusCode)
    
    return message


    
def smdResponce(data = None, method=None):
    
    starusCode = 500
    
    if data != None:
        
        statusCode = 200
        message = getMessage(statusCode, method)
        
        
        responce = {
            "data" : data,
            "message" : message,
            "status" : statusCode
            }
        
    else:
        statusCode = 400
        message = getMessage(statusCode, method)
        
        responce = {
            
            "message" : message,
            "status" : statusCode
            }
    
    return jsonify(responce)





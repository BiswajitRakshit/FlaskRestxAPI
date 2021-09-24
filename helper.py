
import json
from flask import jsonify


def getMessage(statusCode, method):
    
    if statusCode == 400:
        message = "Bad Request, Please don't repeat the Request without modification"
        
    elif statusCode == 200:
        if method == 'get':
            message = "Success, The resource has been fetched and is transmitted in DATA."
            
        if method == 'post':
            message = "Success, The resource has been added and is transmitted in DATA."
            
        if method == 'put':
             message = "OK, The Update Request has succeeded."
             
        if method == 'delete':
            message = "OK, Delete Request deletes the specified resource."
            
        if method == None:
            message = "Action is not found."
            
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





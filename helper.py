from flask import jsonify

def getCustomResponse(success=False, message="Something Went Wrong", data=None, status_code=400):

    if data is None:
        data = []
    response = {
        "success": success,
        "message": message,
        "data": data,
    }
    response = jsonify(response)
    response.status_code=status_code

    return response
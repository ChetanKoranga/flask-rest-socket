import json
from flask import jsonify, make_response

from bson import ObjectId

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)



body = {"status": "", "data": {}, "message": ""}


def success(data=None, statusCode=None, message=None):
    body["status"] = 'Success'
    body["data"] = data
    body["message"] = message
    response = make_response(
        jsonify(json.loads(JSONEncoder().encode(body))),
        statusCode,
    )
    response.headers["content-type"] = "application/json"
    return response


def error( message=None, statusCode=None, data=None):
    body["status"] = 'Failed'
    body["data"] = data
    body["message"] = message
    response = make_response(
        jsonify(json.loads(JSONEncoder().encode(body))),
        statusCode,
    )
    response.headers["content-type"] = "application/json"
    return response

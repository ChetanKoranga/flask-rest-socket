from http.client import BAD_REQUEST, OK
import json
from flask import request
from marshmallow import ValidationError
from app.constants.MessageConstants.MessageConstants import INVALID_PARAMS

from app.utils.requestSchemaValidations.formSchema import FormSchema
from app.utils.responses import error,success 
from ..database.extensions import mongo
from flask_restful import Resource
# from ..resources.errors import SchemaValidationError, MovieAlreadyExistsError, InternalServerError, \
# UpdatingMovieError, DeletingMovieError, MovieNotExistsError


class strategyConfigFormApi(Resource):
    def get(self):
        res = "Configurations Successfully updated"
        # raise SchemaValidationError
        return success(res, "Success")

    def post(self):
        reqParams = request.get_json()
        print(reqParams)
        
        schema = FormSchema()
        try:
            # Validate request body against schema data types
            result = schema.loads(json.dumps(reqParams))
        
        except ValidationError as err:
            print("Schemaa====> ",err.messages)
            # Return a nice message if validation fails
            return error(err.messages, BAD_REQUEST)
        
        # logic for saving the data to the database
        form_collection = mongo.db.formdata
        form_collection.insert_one(reqParams)

    
        msg = "Configurations Successfully updated"

        # return success response
        return success(statusCode=OK,message=msg)

    def put(self):
        return success(statusCode=OK,message="hey I am put method response")

    def patch(self):
        return success(statusCode=OK,message="hey I am patch method response")

    def delete(self):
        return success(statusCode=OK,message="hey I am delete method response")

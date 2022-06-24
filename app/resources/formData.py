from flask import Response, request
from ..database.models import User
from flask_restful import Resource
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from ..resources.errors import SchemaValidationError, MovieAlreadyExistsError, InternalServerError, \
UpdatingMovieError, DeletingMovieError, MovieNotExistsError


class strategyConfigFormApi(Resource):
    def get(self):
        res = "Configurations Successfully updated"
        # raise SchemaValidationError
        return Response(res, mimetype="application/json", status=200)
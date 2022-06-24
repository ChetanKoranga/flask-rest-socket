from flask import Blueprint

from .services.greeksheet import events

main = Blueprint('main', __name__)

# from . import routes

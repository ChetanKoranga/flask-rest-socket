from flask import Blueprint

from .services.greeksheet import events

main = Blueprint("main", __name__)

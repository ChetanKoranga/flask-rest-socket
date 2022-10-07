from flask import Blueprint

from .services import greeksheet,charts

main = Blueprint("main", __name__)

from flask import Flask
from flask_restful import Api
from flask_socketio import SocketIO
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_cors import CORS, cross_origin
from dotenv import load_dotenv

from .database.db import initialize_db
from .resources.routes import initialize_routes
from .resources.errors import errors


load_dotenv()

socketio = SocketIO()

app = Flask(__name__)

CORS(app,allow_headers="*")

# import and implement websocket on app
from .websocketenv import main as main_blueprint
app.register_blueprint(main_blueprint)
socketio.init_app(app,cors_allowed_origins="*")

# 
api = Api(app, errors=errors)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

initialize_db(app)
initialize_routes(api)

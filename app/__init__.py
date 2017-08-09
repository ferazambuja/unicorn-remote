from flask import Flask, request
from flask_restful import Api
import atexit

from app.views import index
from app.state import state
from app.api import SetProgram, StopProgram


app = Flask(__name__)
app.register_blueprint(index)

api = Api(app)
api.add_resource(SetProgram, '/api/program/<string:program_name>')
api.add_resource(StopProgram, '/api/program')

atexit.register(state.stop_program)
from flask import Flask
import os
from flask_cors import CORS

app = Flask(__name__)


from PyPomodoro import routes

cors = CORS(app, resources={r"*": {"origins": "*"}})


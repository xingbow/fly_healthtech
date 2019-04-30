# -*- coding: UTF-8 -*-
from flask import Flask
from flask_cors import CORS
from server.dataService.dataService import DataService

STATIC_FOLDER = '../static'
TEMPLATE_FOLDER = '../client'

app = Flask(__name__, static_url_path='', static_folder=STATIC_FOLDER, template_folder=TEMPLATE_FOLDER)
app.config.from_object('config')
CORS(app)

dataService = DataService()

from server.routes import index

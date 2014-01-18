from flask import Flask, send_from_directory
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from .helpers import JSONEncoder
from flask.ext.restful import Api
import flask.ext.restful.representations.json

import os
db_location = os.getcwd
app = Flask(__name__, static_folder='frontend', static_url_path='')
app.config.from_object('config')
app.json_encoder = JSONEncoder
flask.ext.restful.representations.json.settings["cls"] = JSONEncoder
db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

api_inst = Api(app)

@app.route('/cdn/<path:path>')
def get_ebook_file(path):
    print path
    return send_from_directory(app.config['EBOOK_REPO_PATH'],path)

from api.ebooks import EbookAPI, EbookListAPI, EbookSearchAPI

api_inst.add_resource(EbookListAPI,'/ebooks', endpoint="ebooks")
api_inst.add_resource(EbookAPI, '/ebooks/id/<int:id>', endpoint="ebook")
api_inst.add_resource(EbookSearchAPI, '/ebooks/search', endpoint="search_ebook")


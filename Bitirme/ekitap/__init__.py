from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from collections.abc import Mapping
db = SQLAlchemy()
from flask_cors import CORS
class Config(object):
    SECRET_KEY="test"
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:12345@localhost:5432/ekitap'


def createApp():
    app = Flask(__name__)
    CORS(app, support_credentials=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
    app.config['SECRET_KEY']=Config.SECRET_KEY
    db.init_app(app)
    return app

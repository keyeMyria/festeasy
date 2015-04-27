from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app(env='dev'):
    app = Flask(__name__)
    app.config.from_pyfile('config/default.py')
    db.init_app(app)

    from backend.api import api
    app.register_blueprint(api, url_prefix='/v1')

    return app

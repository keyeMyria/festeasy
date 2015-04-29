from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app(config='dev'):
    app = Flask(__name__)
    app.config.from_pyfile('config/{config}.py'.format(config=config))
    db.init_app(app)

    from backend.api import api
    app.register_blueprint(api, url_prefix='/v1')

    return app

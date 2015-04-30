from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app(config='dev'):
    app = Flask(__name__)
    app.config.from_pyfile('config/{config}.py'.format(config=config))
    db.init_app(app)

    from api.utils import add_cors
    app.after_request(add_cors)

    from backend.api import api
    app.register_blueprint(api, url_prefix='/v1')

    return app

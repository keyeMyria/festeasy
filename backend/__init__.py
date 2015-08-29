import logging
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app(config='live'):
    app = Flask(__name__)
    app.config.from_pyfile('config/{0}.py'.format(config))
    
    db.init_app(app)

    #logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

    from .api.utils import add_cors
    app.after_request(add_cors)

    # Use our custom encoder.
    from backend.utils.custom_json_encoder import CustomJSONEncoder
    app.json_encoder = CustomJSONEncoder

    from backend.api import api
    app.register_blueprint(api, url_prefix='/v1')

    return app

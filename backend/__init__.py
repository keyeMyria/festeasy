import os
import logging
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.cors import CORS


logger = logging.getLogger(__name__)
logger.setLevel(logging.WARN)

db = SQLAlchemy()


def create_app(config):
    app = Flask(__name__)
    CORS(app)

    app.config.from_pyfile('config/default.py'.format(config))

    if config == 'testing':
        app.config.from_pyfile('config/testing.py'.format(config))
    elif config == 'file':
        logger.warn('Loading additional config from backend/config/live.py')
        app.config.from_pyfile('config/live.py'.format(config))
    elif config == 'env':
        logger.warn('Loading additional config from environment variables.')
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["DATABASE_URL"]
    else:
        raise Exception('Unrecognized config paramter.')

    from backend.api import bp
    app.register_blueprint(bp, url_prefix='/api')

    from backend.api import v1_bp
    app.register_blueprint(v1_bp, url_prefix='/api/v1')

    db.init_app(app)

    return app

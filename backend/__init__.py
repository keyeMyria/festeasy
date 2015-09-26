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

    app.config['PROPAGATE_EXCEPTIONS'] = True
    app.config['BUNDLE_ERRORS'] = True

    if config == 'testing':
        app.config['TESTING'] = True
        app.config.from_pyfile('config/testing.py'.format(config))
    elif config == 'file':
        app.config.from_pyfile('config/live.py'.format(config))
        logger.warn('Loading config from config/live.py')
    elif config == 'env':
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["DATABASE_URL"]
        logger.warn('Loading config from environment variables.')
    else:
        raise('No config specified.')

    from backend.api import bp
    app.register_blueprint(bp, url_prefix='/api')

    from backend.api import v1_bp
    app.register_blueprint(v1_bp, url_prefix='/api/v1')

    db.init_app(app)

    return app

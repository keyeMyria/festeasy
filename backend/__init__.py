import os
import logging
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

db = SQLAlchemy()


def create_app(config):
    app = Flask(__name__)

    if config == 'testing':
        app.config.from_pyfile('config/testing.py'.format(config))
        logger.warn('Loading config from config/testing.py')
    elif config == 'file':
        app.config.from_pyfile('config/live.py'.format(config))
        logger.warn('Loading config from config/live.py')
    elif config == 'env':
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["DATABASE_URL"]
        logger.warn('Loading config os.environ: {0}'.format(
                    app.config['SQLALCHEMY_DATABASE_URI'])
                    )
    else:
        raise('No config specified.')

    from backend.api import bp
    app.register_blueprint(bp, url_prefix='/api')

    from backend.api import v1_bp
    app.register_blueprint(v1_bp, url_prefix='/api/v1')

    app.config['BUNDLE_ERRORS'] = True

    db.init_app(app)

    return app

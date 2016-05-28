import os
import logging
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.cors import CORS

from .emailer import Emailer


logger = logging.getLogger(__name__)
logger.setLevel(logging.WARN)

db = SQLAlchemy()
emailer = Emailer()


def create_app(config):
    app = Flask(__name__)
    CORS(app, supports_credentials=True)

    app.config.from_pyfile('config/default.py'.format(config))

    if config == 'testing':
        app.config.from_pyfile('config/testing.py'.format(config))
    elif config == 'file':
        logger.warn('Loading additional config from backend/config/live.py')
        app.config.from_pyfile('config/live.py'.format(config))
    elif config == 'env':
        logger.warn('Loading additional config from environment variables.')
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["DATABASE_URL"]
        app.config['EMAILER_BACKEND'] = os.environ["EMAILER_BACKEND"]
        app.config['MAILGUN_DOMAIN'] = os.environ["MAILGUN_DOMAIN"]
        app.config['MAILGUN_API_KEY'] = os.environ["MAILGUN_API_KEY"]
        app.config['FACEBOOK_SECRET'] = os.environ['FACEBOOK_SECRET']
        app.config['PAYU_SET_TRANSACTION_URL'] = os.environ['PAYU_SET_TRANSACTION_URL']
        app.config['PAYU_NOTIFICATION_URL'] = os.environ['PAYU_NOTIFICATION_URL']
    else:
        raise Exception('Unrecognized config paramter.')

    from backend.api import bp
    app.register_blueprint(bp, url_prefix='/api')

    from backend.api.v1 import v1_bp
    app.register_blueprint(v1_bp, url_prefix='/api/v1')

    from backend.webhooks import webhooks
    app.register_blueprint(webhooks, url_prefix='/webhooks')

    db.init_app(app)
    emailer.init_app(app)

    return app

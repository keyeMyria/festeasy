from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app(config='live'):
    app = Flask(__name__)
    app.config.from_pyfile('config/{0}.py'.format(config))

    from backend.api import bp
    app.register_blueprint(bp, url_prefix='/api')

    from backend.api import v1_bp
    app.register_blueprint(v1_bp, url_prefix='/api/v1')

    app.config['BUNDLE_ERRORS'] = True

    db.init_app(app)

    return app

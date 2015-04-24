from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


def create_app(env='dev'):
	app = Flask(__name__)
	app.config.from_object('config.config')
	return app

import os
from flask.ext.testing import TestCase
from flask import current_app

from backend import create_app, db
from .layers import Layer


class BackendTestCase(TestCase):
    layer = Layer

    def create_app(self):
        app = create_app(config='testing')
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        # Remove FileEmaier file.
        try:
            os.remove(current_app.config['FILE_EMAILER_PATH'])
        except OSError:
            pass

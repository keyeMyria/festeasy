import os
from flask.ext.testing import TestCase
from flask import current_app

from backend import create_app, db


class BackendTestCase(TestCase):
    def drop_all_tables(self):
        db.metadata.reflect(db.engine)
        db.drop_all()

    def create_app(self):
        app = create_app(config='testing')
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        self.drop_all_tables()

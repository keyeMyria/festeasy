from flask.ext.testing import TestCase

from backend import create_app, db


class GeneralTestCase(TestCase):
    def create_app(self):
        app = create_app(config='testing')
        app.config['TESTING'] = True
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

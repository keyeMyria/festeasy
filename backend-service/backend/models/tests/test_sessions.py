import datetime

from backend import db
from backend.testing import ModelTestCase
from backend.testing import factories


class TestSession(ModelTestCase):
    def test_is_valid_with_future_date(self):
        now = datetime.datetime.now()
        future_date = now + datetime.timedelta(days=1)
        session = factories.SessionFactory()
        db.session.add(session)
        db.session.commit()
        session.expires_on = future_date
        self.assertTrue(session.is_valid())

    def test_is_valid_with_past_date(self):
        now = datetime.datetime.now()
        past_date = now - datetime.timedelta(days=1)
        session = factories.SessionFactory()
        session.expires_on = past_date
        db.session.add(session)
        db.session.commit()
        self.assertFalse(session.is_valid())

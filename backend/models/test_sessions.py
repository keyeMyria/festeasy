import datetime

from backend import db
from backend.testing import ModelTestCase
from backend.testing import factories


class TestSession(ModelTestCase):
    def test_is_valid_with_future_date(self):
        now = datetime.datetime.utcnow()
        future_date = now + datetime.timedelta(days=1)
        session = factories.SessionFactory(user=None)
        user = factories.UserFactory()
        db.session.add(user)
        db.session.commit()
        session.expires_on = future_date
        session.user = user
        session.generate_token()
        db.session.add(session)
        db.session.commit()
        self.assertTrue(session.is_valid())

    def test_is_valid_with_past_date(self):
        now = datetime.datetime.utcnow()
        past_date = now - datetime.timedelta(days=1)
        session = factories.SessionFactory(user=None)
        user = factories.UserFactory()
        db.session.add(user)
        db.session.commit()
        session.expires_on = past_date
        session.user = user
        session.generate_token()
        db.session.add(session)
        db.session.commit()
        self.assertFalse(session.is_valid())

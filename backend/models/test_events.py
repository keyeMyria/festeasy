import datetime

from backend import db
from backend.models import Event, User
from backend.models import Cart
from backend.testing import ModelTestCase


class TestEvent(ModelTestCase):
    def test_create_event(self):
        """ Test that an Event can be created.
        """
        event = self.create_event(name='test_event')
        db.session.add(event)
        db.session.commit()

        fetched_event = Event.query.one()
        self.assertEqual(fetched_event, event)


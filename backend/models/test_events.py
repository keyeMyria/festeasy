import datetime

from backend import db
from backend.models import Event, User
from backend.models import UserCartProduct
from backend.utils import ModelTestCase


class TestEvent(ModelTestCase):
    def test_create_event(self):
        """ Test that an Event can be created.
        """
        event = self.create_event(name='test_event')
        db.session.add(event)
        db.session.commit()

        fetched_event = Event.query.one()
        self.assertEqual(fetched_event, event)

    def test_event_deletion_keeps_users(self):
        """ Test that deleting an Event which has 
        users does not delete those users.
        """
        user = self.create_user()
        event = self.create_event(name='test_product', users=[user])
        db.session.add(event)
        db.session.commit()

        self.assertEqual(User.query.one(), user)
        self.assertEqual(User.query.one().current_cart_event, event)

        db.session.delete(event)
        db.session.commit()

        self.assertEqual(User.query.one(), user)
        self.assertIsNone(User.query.one().current_cart_event)


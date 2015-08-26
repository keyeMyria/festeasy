import json
from flask import url_for

from backend import db
from backend.models import User, Product
from backend.testing import APITestCase


class TestGetEvents(APITestCase):
    def test_get_events_returns_events(self):
        """ Test that v1.get_events returns events
        from the db.
        """
        event = self.create_event(name='event_1')
        event_2 = self.create_event(name='event_2')

        db.session.add(event)
        db.session.add(event_2)
        db.session.commit()

        response = self.api_request('get',
            url_for('v1.get_events'),
        )

        self.assertEqual(response.json['events'][0]['id'], event.id)
        self.assertEqual(response.json['events'][1]['id'], event_2.id)

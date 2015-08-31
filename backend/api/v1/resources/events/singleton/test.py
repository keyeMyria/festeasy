from flask import url_for

from backend import db
from backend.testing import APITestCase
from backend.models import Event


endpoint = 'v1.eventsingleton'


class TestEventSingleton(APITestCase):
    def test_get(self):
        event = self.create_event(name='Test')
        db.session.add(event)
        db.session.commit()
        response = self.api_request(
            'get',
            url_for(endpoint, event_id=event.id),
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['id'], event.id)

    def test_delete(self):
        event = self.create_event(name='asdf')
        db.session.add(event)
        db.session.commit()
        response = self.api_request(
            'delete',
            url_for(endpoint, event_id=event.id),
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['id'], event.id)
        self.assertIsNone(Event.query.first())

    def test_patch(self):
        new_name = 'aaa'
        event = self.create_event(name='bbb')
        db.session.add(event)
        db.session.commit()
        response = self.api_request(
            'patch',
            url_for(endpoint, event_id=event.id),
            data=dict(
                name=new_name,
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['name'], new_name)

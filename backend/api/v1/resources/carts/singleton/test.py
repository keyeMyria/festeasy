from flask import url_for

from backend import db
from backend.testing import APITestCase
from backend.models import Cart, Event


class TestCartSingleton(APITestCase):
    def test_get(self):
        cart = Cart()
        db.session.add(cart)
        db.session.commit()
        response = self.api_request(
            'get',
            url_for('v1.cartsingleton', cart_id=cart.id),
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['id'], cart.id)

    def test_patch(self):
        cart = Cart()
        event = Event(name='Test Event')
        db.session.add(cart)
        db.session.add(event)
        db.session.commit()
        response = self.api_request(
            'patch',
            url_for('v1.cartsingleton', cart_id=cart.id),
            data=dict(
                event_id=event.id,
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['event_id'], event.id)

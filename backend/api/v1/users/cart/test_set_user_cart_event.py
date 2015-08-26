import json
from flask import url_for

from backend import db
from backend.models import User, Product, Cart
from backend.testing import APITestCase


class TestSetUserCartEvent(APITestCase):
    def test_set_cart_event_sets_event(self):
        """ Test that v1.set_user_cart_event returns a user
        cart.
        """
        user = self.create_user(create_normal_user=True, create_valid_session=True)
        user.cart = Cart()
        event = self.create_event(name='asd')
        db.session.add(event)
        db.session.add(user)
        db.session.commit()

        response = self.api_request('post',
            url_for('v1.set_user_cart_event', user_id=user.id),
            data=dict(event_id=event.id),
            as_user=user,
            with_session=user.sessions[0],
        )

        self.assertEqual(response.json['cart']['id'], user.cart.id)
        self.assertEqual(response.status_code, 201)

    def test_set_cart_event_404s(self):
        """ Test that v1.set_user_cart_event 404s with 
        invalid event_id.
        """
        user = self.create_user(create_normal_user=True, create_valid_session=True)
        user.cart = Cart()
        event = self.create_event(name='asd')
        db.session.add(event)
        db.session.add(user)
        db.session.commit()

        invalid_event_id = event.id + 1

        response = self.api_request('post',
            url_for('v1.set_user_cart_event', user_id=user.id),
            data=dict(event_id=invalid_event_id),
            as_user=user,
            with_session=user.sessions[0],
        )

        self.assertEqual(response.status_code, 404)

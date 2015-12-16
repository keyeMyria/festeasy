from flask import url_for

from backend import db
from backend.testing import APITestCase, factories
from backend.models import Cart, Festival


endpoint = 'v1.cartsingleton'


class TestCartSingleton(APITestCase):
    def test_get(self):
        cart = factories.CartFactory()
        db.session.add(cart)
        db.session.commit()
        response = self.api_request(
            'get',
            url_for(endpoint, cart_id=cart.id),
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['id'], cart.id)

    def test_patch(self):
        cart = factories.CartFactory()
        festival = factories.FestivalFactory()
        db.session.add(cart)
        db.session.add(festival)
        db.session.commit()
        response = self.api_request(
            'patch',
            url_for(endpoint, cart_id=cart.id),
            data=dict(
                festival_id=festival.id,
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['festival_id'], festival.id)

from backend import db
from backend.models import Cart
from backend.testing import APITestCase, factories


class TestCartSingleton(APITestCase):
    def setUp(self):
        super().setUp()
        self.session = factories.SessionFactory()
        db.session.add(self.session)
        db.session.commit()

    def test_cart_cart_gets_cart(self):
        cart = self.session.user.cart

        self.assertEqual(Cart.query.count(), 1)

        response = self.api_request(
            'get',
            '/api/v1/carts/{cart_id}'.format(cart_id=cart.id),
            session_token=self.session.token
        )

        self.assertEqual(response.status_code, 200, response.json)
        self.assertEqual(response.json['id'], cart.id, response.json)

    def test_patch_cart_patches_cart(self):
        cart = self.session.user.cart
        festival = factories.FestivalFactory()
        db.session.add_all([cart, festival])
        db.session.commit()

        self.assertEqual(cart.festival_id, None)
        self.assertEqual(Cart.query.count(), 1)

        response = self.api_request(
            'patch',
            '/api/v1/carts/{cart_id}'.format(cart_id=cart.id),
            data=dict(festival_id=festival.id),
            session_token=self.session.token,
        )

        self.assertEqual(response.status_code, 200, response.json)
        fetched_cart = Cart.query.one()
        self.assertEqual(fetched_cart.festival_id, festival.id)
        self.assertEqual(
            response.json['festival_id'],
            festival.id,
            response.json,
        )

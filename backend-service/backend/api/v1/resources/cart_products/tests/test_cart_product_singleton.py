from flask import url_for

from backend import db
from backend.testing import APITestCase, factories
from backend.models import CartProduct


endpoint = 'v1.cartproductsingleton'


class TestCartProductSingleton(APITestCase):
    def setUp(self):
        super().setUp()
        self.session = factories.SessionFactory()
        self.cart = factories.CartFactory(user=self.session.user)
        db.session.add_all([self.session, self.cart])
        db.session.commit()

    def test_get(self):
        cart_product = factories.CartProductFactory(
            product=factories.ProductFactory(),
            cart=self.cart,
        )
        db.session.add(cart_product)
        db.session.commit()
        response = self.api_request(
            'get',
            url_for(
                endpoint,
                cart_product_id=cart_product.id
            ),
            session_token=self.session.token,
        )
        self.assertEqual(response.status_code, 200, response.json)
        self.assertEqual(response.json['id'], cart_product.id, response.json)

    def test_patch(self):
        new_quantity = 3
        cart_product = factories.CartProductFactory(
            product=factories.ProductFactory(),
            cart=self.cart,
        )
        db.session.add(cart_product)
        db.session.commit()
        response = self.api_request(
            'patch',
            url_for(
                endpoint,
                cart_product_id=cart_product.id
            ),
            data=dict(
                quantity=new_quantity,
            ),
            session_token=self.session.token,
        )
        self.assertEqual(response.status_code, 200, response.json)
        self.assertEqual(response.json['quantity'], new_quantity, response.json)

    def test_delete(self):
        cart_product = factories.CartProductFactory(
            product=factories.ProductFactory(),
            cart=self.cart,
        )
        db.session.add(cart_product)
        db.session.commit()
        response = self.api_request(
            'delete',
            url_for(endpoint, cart_product_id=cart_product.id),
            session_token=self.session.token,
        )
        self.assertEqual(response.status_code, 200, response.json)
        cart_products = CartProduct.query.all()
        self.assertEqual(cart_products, [], response.json)

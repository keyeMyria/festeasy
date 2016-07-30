from flask import url_for

from backend import db
from backend.models import CartProduct
from backend.testing import APITestCase, factories


endpoint = 'v1.cartproductcollection'


class TestCartProductCollection(APITestCase):
    def test_get(self):
        cart_product = factories.CartProductFactory(
            product=factories.ProductFactory(),
            cart=factories.CartFactory(),
        )
        db.session.add(cart_product)
        db.session.commit()
        response = self.api_request(
            'get',
            url_for(endpoint),
        )
        self.assertEqual(response.status_code, 200, response.json)
        self.assertEqual(response.json[0]['id'], cart_product.id, response.json)

    def test_post(self):
        cart = factories.CartFactory()
        product = factories.ProductFactory()
        db.session.add_all([cart, product])
        db.session.commit()
        data = {
            'cart_id': cart.id,
            'product_id': product.id,
        }
        response = self.api_request(
            'post',
            url_for(endpoint),
            data=data,
        )
        self.assertEqual(response.status_code, 200, response.json)
        fetched_cart_product = CartProduct.query.one()
        self.assertEqual(response.json['id'], fetched_cart_product.id)
        self.assertEqual(fetched_cart_product.cart_id, cart.id)
        self.assertEqual(fetched_cart_product.product_id, product.id)

    def test_post_duplicate(self):
        cart = factories.CartFactory()
        product = factories.ProductFactory()
        cart_product = factories.CartProductFactory(cart=cart, product=product)
        db.session.add_all([cart, product, cart_product])
        db.session.commit()
        data = {
            'cart_id': cart.id,
            'product_id': product.id,
        }
        response = self.api_request(
            'post',
            url_for(endpoint),
            data=data,
        )
        self.assertEqual(response.status_code, 409, response.json)
        self.assertEqual(len(CartProduct.query.all()), 1)

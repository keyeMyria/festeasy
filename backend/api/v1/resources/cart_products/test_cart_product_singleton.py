from flask import url_for

from backend import db
from backend.testing import APITestCase, factories
from backend.models import CartProduct


endpoint = 'v1.cartproductsingleton'


class TestCartProductSingleton(APITestCase):
    def test_get(self):
        cart_product = factories.CartProductFactory(
            product=factories.ProductFactory(),
            cart=factories.CartFactory(),
        )
        db.session.add(cart_product)
        db.session.commit()
        response = self.api_request(
            'get',
            url_for(endpoint,
                    cart_product_id=cart_product.id
                    ),
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['id'], cart_product.id)

    def test_patch(self):
        new_quantity = 3
        cart_product = factories.CartProductFactory(
            product=factories.ProductFactory(),
            cart=factories.CartFactory(),
        )
        db.session.add(cart_product)
        db.session.commit()
        response = self.api_request(
            'patch',
            url_for(endpoint,
                    cart_product_id=cart_product.id
                    ),
            data=dict(
                quantity=new_quantity,
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['quantity'], new_quantity)

    def test_delete(self):
        cart_product = factories.CartProductFactory(
            product=factories.ProductFactory(),
            cart=factories.CartFactory(),
        )
        db.session.add(cart_product)
        db.session.commit()
        response = self.api_request(
            'delete',
            url_for(endpoint, cart_product_id=cart_product.id)
        )
        self.assertEqual(response.status_code, 200)
        cart_products = CartProduct.query.all()
        self.assertEqual(cart_products, [])

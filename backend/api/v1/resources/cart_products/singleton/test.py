from flask import url_for

from backend import db
from backend.testing import APITestCase
from backend.models import CartProduct


class TestCartProductSingleton(APITestCase):
    def test_get(self):
        cart_product = CartProduct(
            product=self.create_product(create_valid_product=True),
            cart=self.create_cart(),
        )
        db.session.add(cart_product)
        db.session.commit()
        response = self.api_request(
            'get',
            url_for('v1.cartproductsingleton',
                    cart_product_id=cart_product.id
            ),
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['id'], cart_product.id)

    def test_patch(self):
        new_quantity = 3
        cart_product = CartProduct(
            product=self.create_product(create_valid_product=True),
            cart=self.create_cart(),
        )
        db.session.add(cart_product)
        db.session.commit()
        response = self.api_request(
            'patch',
            url_for('v1.cartproductsingleton',
                    cart_product_id=cart_product.id
            ),
            data=dict(
                quantity=new_quantity,
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['quantity'], new_quantity)

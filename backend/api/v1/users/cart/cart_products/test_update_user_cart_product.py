import json
from flask import url_for

from backend import db
from backend.models import User, Cart, Product
from backend.models import CartProduct
from backend.testing import APITestCase


class TestUpdateUserCartProducts(APITestCase):
    def test_update_user_cart_product(self):
        """ Test that v1.update_user_cart_product updates quantity.
        """
        user = self.create_user(normal_user=True, valid_session=True)
        product = self.create_product(create_valid_product=True)
        user.cart = Cart(products=[product])
        db.session.add(user)
        db.session.commit()

        cart_product = CartProduct.query.one()
        old_quantity = cart_product.quantity

        new_quantity = old_quantity + 10

        response = self.api_request(
            'patch',
            url_for('v1.update_user_cart_product', user_id=user.id, cart_product_id=cart_product.id), 
            data=dict(quantity=new_quantity),
            as_user=user,
            with_session=user.sessions[0],
        )
        
        self.assertEqual(response.status_code, 201)
        fetched_cart_product = CartProduct.query.one()
        self.assertEqual(fetched_cart_product.quantity, new_quantity)
        self.assertIsNotNone(response.json['cart'])

import json
from flask import url_for

from backend import db
from backend.models import User, Product, Cart
from backend.utils import APITestCase


class TestUpdateCart(APITestCase):
    def test_update_user_cart_update_cart_products_quantity(self):
        """ Test that v1.update_user_cart updates
        cart_product quantity.
        """
        user = self.create_user(create_normal_user=True, create_valid_session=True)
        user.cart = Cart()
        product = self.create_product(name='asd', price_rands=100, cost_rands=10)
        quantity = 10
        cart_product = self.create_cart_product(product=product, quantity=quantity)
        user.cart.cart_products.append(cart_product)
        db.session.add(user)
        db.session.commit()

        new_quantity = quantity - 5

        data = dict(event=None, cart_products=[dict(id=cart_product.id, quantity=new_quantity)])

        response = self.api_request('patch',
            url_for('v1.update_user_cart', user_id=user.id),
            data=data,
            as_user=user,
            with_session=user.sessions[0],
        )

        self.assertEqual(response.json['cart']['cart_products'][0]['quantity'], new_quantity)

    def test_update_user_cart_updates_cart_event(self):
        """ Test that v1.update_user_cart updates
        cart event.
        """
        user = self.create_user(create_normal_user=True, create_valid_session=True)
        user.cart = Cart()
        product = self.create_product(create_valid_product=True)
        event = self.create_event(name='asd')
        user.cart.event = event
        db.session.add(user)
        db.session.commit()

        new_event = self.create_event(name='qwe')
        db.session.add(new_event)
        db.session.commit()

        data = dict(event=dict(id=new_event.id), cart_products=None)

        response = self.api_request('patch',
            url_for('v1.update_user_cart', user_id=user.id),
            data=data,
            as_user=user,
            with_session=user.sessions[0],
        )

        self.assertEqual(response.json['cart']['event']['id'], new_event.id)
    
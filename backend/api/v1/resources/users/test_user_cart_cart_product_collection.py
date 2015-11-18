from flask import url_for

from backend import db
from backend.testing import APITestCase
from backend.models import CartProduct


endpoint = 'v1.usercartcartproductcollection'


class TestUserCartCartProductCollection(APITestCase):
    def test_get(self):
        """
        Test that only a specific user's cart products are returned,
        with a 200 status.
        """
        user = self.create_user(
            normal_user=True,
            with_cart=True,
        )
        cart_product = self.create_cart_product(
            product=self.create_product(create_valid_product=True),
            cart=user.cart,
        )
        other_user = self.create_user(
            normal_user=True,
            with_cart=True,
            email_address='NotTheSame@different.com'
        )
        other_cart_product = self.create_cart_product(
            product=self.create_product(create_valid_product=True),
            cart=other_user.cart,
        )
        db.session.add(user)
        db.session.add(other_user)
        db.session.add(cart_product)
        db.session.add(other_cart_product)
        db.session.commit()
        # TODO: Why does this fail?
        #map(db.session.add, [user, other_user, other_cart_product, cart_product])
        response = self.api_request(
            'get',
            url_for(endpoint, user_id=user.id),
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 1)
        self.assertEqual(response.json[0]['id'], cart_product.id)
        self.assertNotEqual(response.json[0]['id'], other_cart_product.id)

    def test_post(self):
        user = self.create_user(normal_user=True, with_cart=True)
        product = self.create_product(create_valid_product=True)
        db.session.add(user)
        db.session.add(product)
        db.session.commit()
        new_cart_product = {
            'product_id': product.id,
            'cart_id': user.cart.id,
        }
        response = self.api_request(
            'post',
            url_for(endpoint, user_id=user.id),
            data=new_cart_product,
        )
        cart_products = CartProduct.query.all()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(cart_products), 1)
        self.assertEqual(cart_products[0].cart_id, user.cart.id)

from flask import url_for

from backend import db
from backend.testing import APITestCase, factories
from backend.models import CartProduct


endpoint = 'v1.usercartcartproductcollection'


class TestUserCartCartProductCollection(APITestCase):
    def test_get(self):
        """
        Test that only a specific user's cart products are returned,
        with a 200 status.
        """
        user = factories.UserFactory()
        cart_product = factories.CartProductFactory(
            product=factories.ProductFactory(),
            cart=user.cart,
        )
        other_user = factories.UserFactory(
            email_address='NotTheSame@different',
        )
        other_cart_product = factories.CartProductFactory(
            product=factories.ProductFactory(),
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
        self.assertEqual(response.status_code, 200, response.json)
        self.assertEqual(len(response.json), 1, response.json)
        self.assertEqual(
            response.json[0]['id'],
            cart_product.id,
            response.json,
        )
        self.assertNotEqual(
            response.json[0]['id'],
            other_cart_product.id,
            response.json,
        )

    def test_post(self):
        user = factories.UserFactory()
        product = factories.ProductFactory()
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
        self.assertEqual(response.status_code, 200, response.json)
        self.assertEqual(len(cart_products), 1, response.json)
        self.assertEqual(cart_products[0].cart_id, user.cart.id, response.json)

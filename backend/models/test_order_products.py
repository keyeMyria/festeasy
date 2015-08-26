import datetime

from backend import db
from backend.models import Session, User, Product
from backend.models import Cart, Order
from backend.models import OrderProduct
from backend.testing import ModelTestCase


class TestOrderProduct(ModelTestCase):
    def test_product_order_creation(self):
        """ Test that a OrderProduct can be created.
        """
        user = self.create_user(create_normal_user=True, create_valid_cart=True)
        product = self.create_product(create_valid_product=True)
        event = self.create_event(name='asd')
        order = self.create_order(event=event, user=user)
        
        order_product = OrderProduct(
            order=order,
            product=product,
            unit_price_rands=product.price_rands,
            quantity=1,
            )

        db.session.add(order_product)
        db.session.add(order)
        db.session.commit()

        fetched_order = Order.query.one()

        self.assertEqual(fetched_order, order)
        self.assertEqual(fetched_order.products, [product])

    def test_order_product_deletion(self):
        """ Test that a OrderProduct deletion does not delete
        the user nor product nor event.
        """
        user = self.create_user(create_normal_user=True, create_valid_cart=True)
        product = self.create_product(create_valid_product=True)
        event = self.create_event(name='asd')
        order = self.create_order()

        order.event = event
        order.user = user
        order_product = OrderProduct(
            order=order,
            product=product,
            unit_price_rands=product.price_rands,
            quantity=1,
            )

        db.session.add(order_product)
        db.session.add(order)
        db.session.commit()

        fetched_order = Order.query.one()

        self.assertEqual(fetched_order, order)
        self.assertEqual(fetched_order.user, user)
        self.assertEqual(fetched_order.products, [product])
        self.assertEqual(fetched_order.event, event)

        fetched_order_product = OrderProduct.query.one()
        db.session.delete(fetched_order_product)

        self.assertEqual(OrderProduct.query.all(), list())
        self.assertEqual(User.query.one(), user)
        self.assertEqual(Product.query.one(), product)
        self.assertEqual(Order.query.one(), order)

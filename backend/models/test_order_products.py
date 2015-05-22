import datetime

from backend import db
from backend.models import Session, User, Product
from backend.models import UserCartProduct, Order
from backend.models import OrderProduct
from backend.utils import ModelTestCase


class TestOrderProduct(ModelTestCase):
    def test_product_order_creation(self):
        """ Test that a OrderProduct can be created.
        """
        user = self.create_user()
        product = self.create_product(name='abc', price_rands=99)
        order = self.create_order()
        event = self.create_event(name='asd')

        order.event = event
        order.user = user

        order_product = OrderProduct(
            order=order,
            product=product,
            price_rands=product.price_rands,
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
        user = self.create_user()
        product = self.create_product(name='abc', price_rands=99)
        event = self.create_event(name='asd')
        order = self.create_order()

        order.event = event
        order.user = user
        order_product = OrderProduct(
            order=order,
            product=product,
            price_rands=product.price_rands,
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

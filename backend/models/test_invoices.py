import datetime

from backend import db
from backend.models import Event, User, Order
from backend.models import Cart, InvoiceProduct, Invoice
from backend.utils import ModelTestCase


class TestOrder(ModelTestCase):
    def test_create_invoice(self):
        """ Test that an Invoice can be created
        """
        user = self.create_user()
        product = self.create_product(name='qwe', price_rands=99)
        order = self.create_order()
        event = self.create_event(name='asd')
        user.cart.event = event
        user.cart.products.append(product)
        order.from_cart(user.cart)
        db.session.add(order)
        db.session.commit()

        invoice_product = InvoiceProduct(product=product, quantity=1, unit_price_rands=99)
        invoice = Invoice(
            order=order,
            invoice_products=[invoice_product],
            )
        db.session.add(invoice)
        db.session.commit()

        fetched_invoice = Invoice.query.one()

        self.assertEqual(fetched_invoice.total_rands, 99)
        self.assertEqual(fetched_invoice.products, [product])

    def test_from_order(self):
        user = self.create_user()
        product_price = 99
        product = self.create_product(name='qwe', price_rands=product_price)
        order = self.create_order()
        event = self.create_event(name='asd')
        user.cart.event = event
        user.cart.products.append(product)
        # TODO: Look into why this is needed:
        db.session.add(user)
        db.session.commit()
        order.from_cart(user.cart)
        db.session.add(order)
        db.session.commit()

        invoice = Invoice()
        invoice.from_order(order)

        db.session.add(invoice)
        db.session.commit()

        fetched_invoice = Invoice.query.one()

        self.assertEqual(fetched_invoice.total_rands, product_price)
        self.assertEqual(fetched_invoice.products, [product])
        
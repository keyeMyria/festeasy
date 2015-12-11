from backend import db
from backend.models import Invoice, Order
from backend.testing import ModelTestCase


class TestInvoice(ModelTestCase):
    def test_from_order(self):
        """
        Test that Invoice.from_order sets up an Invoice from an
        Order correctly.
        """
        price = 99
        user = self.create_user(normal_user=True, with_cart=True)
        product = self.create_product(
            create_valid_product=True,
            product_prices=[
                self.create_product_price(
                    amount_rands=price,
                )
            ],
        )
        festival = self.create_festival(
            pre_populate=True,
            name='asd',
            base_festival=self.create_base_festival(),
        )
        user.cart.festival = festival
        user.cart.products.append(product)
        db.session.add(user)
        db.session.commit()
        order = Order.from_cart(user.cart)
        db.session.add(order)
        db.session.commit()
        invoice = Invoice.from_order(order)
        db.session.add(invoice)
        db.session.commit()
        fetched_invoice = Invoice.query.first()
        self.assertEqual(fetched_invoice.total_rands, price)
        self.assertEqual(fetched_invoice.products, order.products)
        self.assertEqual(fetched_invoice.products, [product])

    def test_invoice_total_rands(self):
        """ Test that Invoice.total_rands is correct.
        """
        price = 99
        user = self.create_user(normal_user=True, with_cart=True)
        product = self.create_product(
            create_valid_product=True,
            product_prices=[
                self.create_product_price(
                    amount_rands=price,
                )
            ],
        )
        festival = self.create_festival(
            pre_populate=True,
            name='asd',
            base_festival=self.create_base_festival(),
        )
        user.cart.festival = festival
        user.cart.products.append(product)
        db.session.add(user)
        db.session.commit()
        order = Order.from_cart(user.cart)
        db.session.add(order)
        db.session.commit()
        invoice = Invoice.from_order(order)
        db.session.add(invoice)
        db.session.commit()
        fetched_invoice = Invoice.query.first()
        self.assertEqual(fetched_invoice.total_rands, price)

    def test_invoice_amount_due_rands_with_payment(self):
        """ Test that Invoice.amount_due_rands is correct with a Payment.
        """
        price = 99
        user = self.create_user(normal_user=True, with_cart=True)
        product = self.create_product(
            create_valid_product=True,
            product_prices=[
                self.create_product_price(
                    amount_rands=price,
                )
            ],
        )
        festival = self.create_festival(
            pre_populate=True,
            name='asd',
            base_festival=self.create_base_festival(),
        )
        user.cart.festival = festival
        user.cart.products.append(product)
        db.session.add(user)
        db.session.commit()
        order = Order.from_cart(user.cart)
        db.session.add(order)
        db.session.commit()
        invoice = Invoice.from_order(order)
        db.session.add(invoice)
        db.session.commit()
        payment = self.create_payment(
            amount_rands=price - 9,
            invoice=invoice,
        )
        db.session.add(payment)
        db.session.commit()
        fetched_invoice = Invoice.query.first()
        self.assertEqual(fetched_invoice.amount_due_rands, 9)

    def test_invoice_amount_due_rands_with_no_payment(self):
        """ Test that Invoice.amount_due_rands is correct with no Payments.
        """
        price = 99
        user = self.create_user(normal_user=True, with_cart=True)
        product = self.create_product(
            create_valid_product=True,
            product_prices=[
                self.create_product_price(
                    amount_rands=price,
                )
            ],
        )
        festival = self.create_festival(
            pre_populate=True,
            name='asd',
            base_festival=self.create_base_festival(),
        )
        user.cart.festival = festival
        user.cart.products.append(product)
        db.session.add(user)
        db.session.commit()
        order = Order.from_cart(user.cart)
        db.session.add(order)
        db.session.commit()
        invoice = Invoice.from_order(order)
        db.session.add(invoice)
        db.session.commit()
        fetched_invoice = Invoice.query.first()
        self.assertEqual(fetched_invoice.amount_due_rands, price)

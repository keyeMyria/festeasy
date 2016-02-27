from backend import db
from backend.testing import ModelTestCase
from backend.testing import factories

from . import Invoice, Order, InvoiceProduct


class TestInvoice(ModelTestCase):
    def test_from_order(self):
        """
        Test that Invoice.from_order sets up an Invoice from an
        Order correctly.
        """
        price = 10
        user = factories.UserFactory()
        product_1 = factories.ProductFactory(price_rands=price)
        product_2 = factories.ProductFactory(price_rands=price)
        festival = factories.FestivalFactory()
        user.cart.festival = festival
        cart_product_1 = factories.CartProductFactory(
            cart=user.cart,
            product=product_1,
            quantity=2,
        )
        cart_product_2 = factories.CartProductFactory(
            cart=user.cart,
            product=product_2,
            quantity=3,
        )
        db.session.add(cart_product_1)
        db.session.add(cart_product_2)
        db.session.add(user)
        db.session.commit()

        order = Order.from_cart(user.cart)
        db.session.add(order)
        db.session.commit()

        invoice = Invoice.from_order(order)
        db.session.add(invoice)
        db.session.commit()

        fetched_invoice = Invoice.query.first()
        self.assertEqual(fetched_invoice.total_rands, 5 * price)
        self.assertEqual(fetched_invoice.products, order.products)

        ip1 = (InvoiceProduct.query.filter(
            InvoiceProduct.product == product_1)
            .first())
        self.assertEqual(ip1.quantity, 2)

        ip2 = (InvoiceProduct.query.filter(
            InvoiceProduct.product == product_2)
            .first())
        self.assertEqual(ip2.quantity, 3)

    def test_invoice_total_rands(self):
        """ Test that Invoice.total_rands is correct.
        """
        price = 99
        user = factories.UserFactory()
        product = factories.ProductFactory(price_rands=price)
        festival = factories.FestivalFactory()
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
        user = factories.UserFactory()
        product = factories.ProductFactory(price_rands=price)
        festival = factories.FestivalFactory()
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
        payment = factories.PaymentFactory(
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
        user = factories.UserFactory()
        product = factories.ProductFactory(price_rands=price)
        festival = factories.FestivalFactory()
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

import datetime
from flask.ext.testing import TestCase

from backend import create_app, db
from backend.models import User, Session, Product
from backend.models import Festival, Order, Cart, Invoice
from backend.models import OrderProduct, CartProduct, BaseFestival
from backend.models import Payment, InvoiceProduct, Category, ProductPrice
from backend.testing.utils import template_entity


class BackendTestCase(TestCase):
    def create_app(self):
        app = create_app(config='testing')
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def create_product_price(self, *args, **kwargs):
        product_price = ProductPrice(*args, **kwargs)
        return product_price

    def create_category(self, *args, **kwargs):
        category = Category(*args, **kwargs)
        return category

    def create_cart(self, *args, **kwargs):
        cart = Cart(*args, **kwargs)
        return cart

    def create_payment(self, *args, **kwargs):
        payment = Payment(*args, **kwargs)
        return payment

    def create_invoice(self, *args, **kwargs):
        invoice = Invoice(*args, **kwargs)
        return invoice

    def create_invoice_product(self, *args, **kwargs):
        invoice_product = InvoiceProduct(*args, **kwargs)
        return invoice_product

    def create_cart_product(self, *args, **kwargs):
        cart_product = CartProduct(*args, **kwargs)
        return cart_product

    def create_order_product(self, *args, **kwargs):
        order_product = OrderProduct(*args, **kwargs)
        return order_product

    def create_order(self, *args, **kwargs):
        order = Order(*args, **kwargs)
        return order

    def create_base_festival(self, *args, **kwargs):
        base_festival = BaseFestival(*args, **kwargs)
        return base_festival

    def create_festival(self, *args, pre_populate=False, **kwargs):
        if pre_populate:
            template = {
                'name': 'My Festival',
            }
            kwargs = template_entity(template, kwargs)
            now = datetime.datetime.now()
            if 'starts_on' not in kwargs:
                kwargs['starts_on'] = now + datetime.timedelta(days=8)
        festival = Festival(*args, **kwargs)
        return festival

    def create_product(self, *args, create_valid_product=None, **kwargs):
        product = Product(*args, **kwargs)
        if create_valid_product:
            if 'name' not in kwargs.keys():
                product.name = 'Auto Product'
            if 'cost_rands' not in kwargs.keys():
                product.cost_rands = 88.12345
            if 'product_prices' not in kwargs.keys():
                product.product_prices.append(
                    ProductPrice(
                        amount_rands=12.1234,
                    )
                )
        return product

    def create_session(self, *args, valid_session=False, **kwargs):
        now = datetime.datetime.now()
        if valid_session:
            session_template = {
                'expires_on': now,
            }
            kwargs = template_entity(session_template, kwargs)
        session = Session(*args, **kwargs)
        if valid_session:
            session.generate_token()
        return session

    def create_user(self, *args, normal_user=False,
            valid_session=False, with_cart=False, **kwargs):
        now = datetime.datetime.now()
        if normal_user:
            user_template = {
                'email_address': 'auto-test@festeasy.co.za',
                'password': 'autotest_password',
                'first_name': 'autotest_first_name',
            }
            kwargs = template_entity(user_template, kwargs)
        user = User(*args, **kwargs)

        if valid_session:
            expires_on = now + datetime.timedelta(seconds=30)
            session = self.create_session(
                expires_on=expires_on,
                user=user,
            )
            session.generate_token()
            user.sessions.append(session)
        if with_cart:
            user.cart = Cart()
        return user

import datetime
from flask.ext.testing import TestCase

from backend import create_app, db
from backend.utils.random_string import random_string
from backend.models import User, Session, Product
from backend.models import Event, Order, Cart, Invoice
from backend.models import OrderProduct, CartProduct
from backend.models import Payment
from backend.testing.utils import template_entity


class GeneralTestCase(TestCase):
    def create_app(self):
        app = create_app(config='testing')
        app.config['TESTING'] = True
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def create_payment(self, *args, **kwargs):
        payment = Payment(*args, **kwargs)
        return payment

    def create_invoice(self, *args, **kwargs):
        invoice = Invoice(*args, **kwargs)
        return invoice

    def create_cart_product(self, *args, **kwargs):
        cart_product = CartProduct(*args, **kwargs)
        return cart_product

    def create_order_product(self, *args, **kwargs):
        order_product = OrderProduct(*args, **kwargs)
        return order_product

    def create_order(self, *args, **kwargs):
        order = Order(*args, **kwargs)
        return order

    def create_event(self, *args, **kwargs):
        event = Event(*args, **kwargs)
        return event

    def create_product(self, *args, create_valid_product=None, **kwargs):
        if create_valid_product:
            product_template = {
                'name': 'Auto Product',
                'price_rands': 999.12345,
                'cost_rands': 88.12345
            }
            kwargs = template_entity(product_template, kwargs)
        product = Product(*args, **kwargs)
        return product

    def create_session(self, *args, create_valid_session=False, **kwargs):
        now = datetime.datetime.now()
        if create_valid_session:
            session_template = {
                'expires_on': now,
                'token': random_string(25),
            }
            kwargs = template_entity(session_template, kwargs)
        session = Session(*args, **kwargs)
        return session

    def create_user(self, *args, create_normal_user=False, create_valid_session=False, create_valid_cart=False, **kwargs):
        now = datetime.datetime.now()
        if create_normal_user:
            user_template = {
                'email_address': 'auto-test@festeasy.co.za',
                'password': 'autotest_password',
                'first_name': 'autotest_first_name',
            }
            kwargs = template_entity(user_template, kwargs)
        user = User(*args, **kwargs)
        
        if create_valid_session:
            expires_on = now + datetime.timedelta(seconds=30)
            token = random_string(25)
            session = self.create_session(expires_on=expires_on, token=token)
            user.sessions.append(session)

        if create_valid_cart:
            user.cart = Cart()
        return user

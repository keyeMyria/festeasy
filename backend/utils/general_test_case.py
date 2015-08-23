import datetime
from flask.ext.testing import TestCase

from backend import create_app, db
from backend.utils.random_string import random_string
from backend.models import User, Session, Product
from backend.models import Event, Order, Cart, Invoice
from backend.models import OrderProduct, CartProduct
from backend.models import Payment


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

    def create_payment(self, *args, **kwagrs):
        payment = Payment(*args, **kwagrs)
        return payment

    def create_invoice(self, *args, **kwagrs):
        invoice = Invoice(*args, **kwagrs)
        return invoice

    def create_cart_product(self, *args, **kwagrs):
        cart_product = CartProduct(*args, **kwagrs)
        return cart_product

    def create_order_product(self, *args, **kwagrs):
        order_product = OrderProduct(*args, **kwagrs)
        return order_product

    def create_order(self, *args, **kwagrs):
        order = Order(*args, **kwagrs)
        return order

    def create_event(self, *args, **kwagrs):
        event = Event(*args, **kwagrs)
        return event

    def create_product(self, *args, create_valid_product=None, **kwagrs):
        if create_valid_product:
            if 'name' not in kwagrs.keys():
                kwagrs['name'] = 'Auto Product'
            if 'price_rands' not in kwagrs.keys():
                kwagrs['price_rands'] = 99999.12345
            kwagrs['cost_rands'] = 10
        product = Product(*args, **kwagrs)
        return product

    def create_session(self, expires_on=None, token=None, user=None, create_valid_session=False):
        now = datetime.datetime.now()
        if create_valid_session:
            expires_on = now + datetime.timedelta(seconds=30)
            token = random_string(25)
        session = Session(expires_on=expires_on, user=user, token=token)
        return session

    def create_user(self, email_address=None, create_normal_user=False, is_admin=False,
        password=None, cart=None, guest_token=None, first_name=None, create_valid_session=False, create_cart=True, orders=[]):
        now = datetime.datetime.now()
        if create_normal_user:
            if not email_address:
                email_address = 'test@festeasy.co.za'
            if not password:
                password = 'qwe'
            if not first_name:
                first_name = 'Jason'

        user = User(email_address=email_address, password=password, cart=cart, is_admin=is_admin,
            guest_token=guest_token, first_name=first_name, orders=orders)
        
        if create_valid_session:
            expires_on = now + datetime.timedelta(seconds=30)
            token = random_string(25)
            session = self.create_session(expires_on=expires_on, token=token)
            user.sessions.append(session)
        if create_cart:
            user.cart = Cart()
        return user

import datetime
from sqlalchemy import Column, Integer
from sqlalchemy import DateTime

from backend import db


class Entity(object):
    id = Column(Integer, primary_key=True)
    created_on = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        nullable=False,
    )
    last_updated_on = db.Column(
        db.DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
        nullable=False,
    )

# All the models
from .session import Session
from .user import User
from .product import Product
from .event import Event
from .order_product import OrderProduct
from .order import Order
from .cart_product import CartProduct
from .cart import Cart
from .invoice_product import InvoiceProduct
from .payment import Payment
from .invoice import Invoice

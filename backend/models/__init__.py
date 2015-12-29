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
from .sessions import Session
from .users import User
from .product_prices import ProductPrice
from .products import Product
from .festivals import Festival
from .order_products import OrderProduct
from .orders import Order
from .cart_products import CartProduct
from .carts import Cart
from .invoice_products import InvoiceProduct
from .payments import Payment
from .invoices import Invoice
from .categories import Category
from .product_categories import ProductCategory
from .base_festivals import BaseFestival
from .suppliers import Supplier
from .base_suppliers import BaseSupplier
from .product_suppliers import ProductSupplier
from .product_stocks import ProductStock
from .forgot_password_tokens import ForgotPasswordToken

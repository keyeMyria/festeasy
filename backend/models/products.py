import datetime
from sqlalchemy import Column, Integer, String, DateTime, Numeric
from sqlalchemy import Boolean
from sqlalchemy.orm import relationship

from backend import db
from backend.models import Entity, Dumpable


class Product(db.Model, Entity, Dumpable):
    __tablename__ = 'product'

    whitelist = [
        'id',
        'created_on',
        'name',
        'price_rands',
        'cost_rands',
        'is_enabled',
    ]
    
    name = Column(String(150), nullable=False)
    # The price of a Product in Rands.
    price_rands = Column(Numeric, nullable=False)
    # The cost of a Product in Rands.
    cost_rands = Column(Numeric, nullable=False)
    # Should a Product show up on the products list.
    is_enabled = Column(Boolean, default=False, nullable=False)

    carts = relationship('Cart', secondary='cart_product', back_populates='products',
        cascade='save-update, merge')
    cart_products = relationship('CartProduct', back_populates='product',
        cascade='save-update, merge, delete')

    orders = relationship('Order', secondary='order_product', back_populates='products',
        cascade='save-update, merge')
    order_products = relationship('OrderProduct', back_populates='product',
        cascade='save-update, merge')

    invoices = relationship('Invoice', secondary='invoice_product', back_populates='products')
    invoice_products = relationship('InvoiceProduct', back_populates='product')

    def __init__(self, is_enabled=None, name=None, price_rands=None, cost_rands=None, orders=[], order_products=[]):
        self.is_enabled = is_enabled
        self.name = name
        self.price_rands = price_rands
        self.cost_rands = cost_rands
        self.orders = orders
        self.order_products = order_products

    def __repr__(self):
        return '<Product {id}>'.format(id=self.id)

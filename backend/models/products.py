import datetime
from sqlalchemy import Column, Integer, String, DateTime, Numeric
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
    ]
    
    name = Column(String(150), nullable=False)
    price_rands = Column(Numeric, nullable=False)
    cost_rands = Column(Numeric, nullable=False)

    carts = relationship('Cart', secondary='cart_product',
        cascade='save-update, merge')

    orders = relationship('Order', secondary='order_product',
        cascade='save-update, merge')

    order_products = relationship('OrderProduct',
        cascade='save-update, merge')

    def __init__(self, name=None, cost_rands=None, price_rands=None, orders=[], order_products=[]):
        self.name = name
        self.cost_rands = cost_rands
        self.price_rands = price_rands
        self.orders = orders
        self.order_products = order_products

    def __repr__(self):
        return '<Product {id}>'.format(id=self.id)

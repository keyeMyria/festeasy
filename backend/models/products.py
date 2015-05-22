import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float
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
    price_rands = Column(Float, nullable=False)
    cost_rands = Column(Float, nullable=False)

    cart_users = relationship('User', secondary='user_cart_product',
        cascade='save-update, merge')

    user_cart_products = relationship('UserCartProduct',
        cascade='save-update, merge, delete, delete-orphan')

    orders = relationship('Order', secondary='order_product',
        cascade='save-update, merge')

    order_products = relationship('OrderProduct',
        cascade='save-update, merge')

    def __init__(self, name=None, cost_rands=None, price_rands=None, cart_users=[], orders=[], order_products=[]):
        self.name = name
        self.cost_rands = cost_rands
        self.price_rands = price_rands
        self.cart_users = cart_users
        self.orders = orders
        self.order_products = order_products

    def __repr__(self):
        return '<Product {id}>'.format(id=self.id)

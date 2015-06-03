import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from backend import db
from backend.models import Entity, Dumpable


class Order(db.Model, Entity, Dumpable):
    __tablename__ = 'order'

    whitelist = [
        'id',
        'created_on',
        'event',
        'order_products',
        'total_rands',
    ]

    @property
    def total_rands(self):
        total_rands = 0
        for order_product in self.order_products:
            total_rands += order_product.sub_total_rands
        return total_rands
    
    event_id = Column(Integer, ForeignKey('event.id'), nullable=False)
    event = relationship('Event', back_populates='orders',
        cascade='save-update, merge')

    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User', back_populates='orders',
        cascade='save-update, merge')

    invoices = relationship('Invoice', back_populates='order')

    products = relationship('Product', secondary='order_product', back_populates='orders',
        cascade='save-update, merge')

    order_products = relationship('OrderProduct', back_populates='order',
        cascade='save-update, merge')

    def __init__(self, event=None, user=None, products=[], order_products=[]):
        self.event = event
        self.user = user
        self.products = products
        self.order_products = order_products

    def __repr__(self):
        return '<Order {id}>'.format(id=self.id)

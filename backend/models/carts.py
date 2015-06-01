import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from backend import db
from backend.models import Entity, Dumpable


class Cart(db.Model, Entity, Dumpable):
    __tablename__ = 'cart'

    whitelist = [
        'id',
        'created_on',
        'event',
        'products',
        'cart_products',
    ]
    
    event_id = Column(Integer, ForeignKey('event.id'))
    event = relationship('Event', back_populates='carts',
        cascade='save-update, merge')

    user = relationship('User', back_populates='cart', uselist=False,
        cascade='save-update, merge')

    products = relationship('Product', secondary='cart_product',
        cascade='save-update, merge')

    cart_products = relationship('CartProduct',
        cascade='save-update, merge')

    def __init__(self, event=None, user=None, products=[]):
        self.event = event
        self.user = user
        self.products = products

    def __repr__(self):
        return '<Cart {id}>'.format(id=self.id)

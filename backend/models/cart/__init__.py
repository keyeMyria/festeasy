import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy import ForeignKey, func, select
from sqlalchemy.orm import relationship, column_property

from backend import db
from backend.models import Entity, Dumpable, CartProduct
from backend.models import Event


class Cart(db.Model, Entity, Dumpable):
    __tablename__ = 'cart'

    whitelist = [
        'id',
        'created_on',
        'selectable_events',
        'event',
        'products',
        'cart_products',
        'total_rands',
        'number_of_items',
    ]

    def __init__(self, event=None, user=None, products=[]):
        self.event = event
        self.user = user
        self.products = products

    def __repr__(self):
        return '<Cart {id}>'.format(id=self.id)

    event_id = Column(Integer, ForeignKey('event.id'))
    event = relationship(
        'Event',
        back_populates='carts',
        cascade='save-update, merge'
    )
    user = relationship(
        'User',
        back_populates='cart',
        uselist=False,
        cascade='save-update, merge'
    )
    products = relationship(
        'Product',
        secondary='cart_product',
        back_populates='carts',
        cascade='save-update, merge'
    )
    cart_products = relationship(
        'CartProduct',
        back_populates='cart',
        cascade='save-update, merge, delete, delete-orphan'
    )

    @property
    def selectable_events(self):
        selectable_events = Event.query.all()
        return selectable_events

    @property
    def number_of_items(self):
        return len(self.cart_products)

Cart.total_rands = column_property(
    select([func.sum(CartProduct.sub_total_rands)]).where(
        CartProduct.cart_id == Cart.id).correlate(Cart)
)

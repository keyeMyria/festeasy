from sqlalchemy import Column, Integer
from sqlalchemy import ForeignKey, func, select
from sqlalchemy.orm import relationship, column_property

from backend import db
from backend.models import Entity, CartProduct
from backend.models import Festival


class Cart(db.Model, Entity):
    __tablename__ = 'cart'

    def __init__(self, festival=None, user=None, products=[]):
        self.festival = festival
        self.user = user
        self.products = products

    def __repr__(self):
        return '<Cart {id}>'.format(id=self.id)

    festival_id = Column(Integer, ForeignKey('festival.id'))
    festival = relationship(
        'Festival',
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
    def total_rands(self):
        total_rands = 0
        for cart_product in self.cart_products:
            total_rands += cart_product.sub_total_rands
        return total_rands

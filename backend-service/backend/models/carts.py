from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from backend import db
from backend.models.utils import Entity


class Cart(db.Model, Entity):
    def __repr__(self):
        return '<Cart {self.id}>'.format(self=self)

    festival_id = Column(Integer, ForeignKey('festival.id'))
    festival = relationship(
        'Festival',
        back_populates='carts',
    )

    user = relationship(
        'User',
        back_populates='cart',
        uselist=False,
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

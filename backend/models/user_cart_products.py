import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

from backend import db
from backend.models import Entity, Dumpable


class UserCartProduct(db.Model, Entity, Dumpable):
    __tablename__ = 'user_cart_product'

    whitelist = [
        'id',
        'created_on',
        'quantity',
        'product',
        'sub_total_rands',
    ]

    @property
    def sub_total_rands(self):
        return self.product.price_rands * self.quantity 

    quantity = Column(Integer, default=1, nullable=False)

    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User', cascade='save-update, merge')

    product_id = Column(Integer, ForeignKey('product.id'), nullable=False)
    product = relationship('Product', cascade='save-update, merge')

    __table_args__ = (
        UniqueConstraint('user_id', 'product_id'),
    )

    def __init__(self, quantity=None, user=None, product=None):
        self.quantity = quantity
        self.user = user
        self.product = product

    def __repr__(self):
        return '<UserCartProduct {id}>'.format(id=self.id)

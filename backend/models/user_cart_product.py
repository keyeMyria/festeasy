import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from backend import db
from backend.models import Entity, Dumpable


class UserCartProduct(db.Model, Entity, Dumpable):
    __tablename__ = 'user_cart_product'

    whitelist = [
        'id',
        'created_on',
    ]

    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', cascade='save-update, merge')

    product_id = Column(Integer, ForeignKey('product.id'))
    product = relationship('Product', cascade='save-update, merge')

    def __repr__(self):
        return '<Cart {id}>'.format(id=self.id)
import datetime
from sqlalchemy import Column, Integer, String, DateTime, Numeric
from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

from backend import db
from backend.models import Entity, Dumpable


class CartProduct(db.Model, Entity, Dumpable):
    __tablename__ = 'cart_product'

    whitelist = [
        'id',
        'created_on',
        'product',
        'quantity',
        'sub_total_rands',
    ]

    @property
    def sub_total_rands(self):
        return self.product.price_rands * self.quantity

    quantity = Column(Integer, default=1, nullable=False)

    product_id = Column(Integer, ForeignKey('product.id'), nullable=False)
    product = relationship('Product', back_populates='cart_products',
        cascade='save-update, merge')

    cart_id = Column(Integer, ForeignKey('cart.id'), nullable=False)
    cart = relationship('Cart', back_populates='cart_products')

    __table_args__ = (
        UniqueConstraint('cart_id', 'product_id'),
    )

    def __init__(self, quantity=None, product=None, cart=None):
        self.quantity = quantity
        self.product = product
        self.cart = cart

    def __repr__(self):
        return '<CartProduct {id}>'.format(id=self.id)

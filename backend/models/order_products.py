import datetime
from sqlalchemy import Column, Integer, String, DateTime, Numeric
from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

from backend import db
from backend.models import Entity, Dumpable


class OrderProduct(db.Model, Entity, Dumpable):
    __tablename__ = 'order_product'

    whitelist = [
        'id',
        'created_on',
        'product',
        'unit_price_rands',
        'quantity',
        'sub_total_rands',
    ]

    @property
    def sub_total_rands(self):
        return self.unit_price_rands * self.quantity

    unit_price_rands = Column(Numeric, nullable=False)
    quantity = Column(Integer, nullable=False)

    order_id = Column(Integer, ForeignKey('order.id'), nullable=False)
    order = relationship('Order', cascade='save-update, merge')

    product_id = Column(Integer, ForeignKey('product.id'), nullable=False)
    product = relationship('Product', cascade='save-update, merge')

    __table_args__ = (
        UniqueConstraint('order_id', 'product_id'),
    )

    def __init__(self, unit_price_rands=None, quantity=None, order=None, product=None):
        self.unit_price_rands = unit_price_rands
        self.quantity = quantity
        self.order = order
        self.product = product

    def __repr__(self):
        return '<OrderProduct {id}>'.format(id=self.id)

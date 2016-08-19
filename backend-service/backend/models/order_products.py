from sqlalchemy import Column, Integer, Numeric, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

from backend import db

from .utils import Entity


class OrderProduct(db.Model, Entity):
    def __repr__(self):
        return '<OrderProduct {self.id}>'.format(self=self)

    unit_price_rands = Column(Numeric, nullable=False)
    quantity = Column(Integer, nullable=False)

    order_id = Column(ForeignKey('order.id'), nullable=False)
    order = relationship(
        'Order',
        back_populates='order_products',
    )

    product_id = Column(ForeignKey('product.id'), nullable=False)
    product = relationship(
        'Product',
        back_populates='order_products',
    )

    @property
    def sub_total_rands(self):
        return self.quantity * self.unit_price_rands

    __table_args__ = (
        UniqueConstraint('order_id', 'product_id'),
    )

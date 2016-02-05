from sqlalchemy import Column, Integer, Numeric
from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

from backend import db

from .utils import Entity


class OrderProduct(db.Model, Entity):
    __tablename__ = 'order_product'

    def __repr__(self):
        return '<OrderProduct {id}>'.format(id=self.id)

    @property
    def sub_total_rands(self):
        return self.quantity * self.unit_price_rands

    unit_price_rands = Column(Numeric, nullable=False)
    quantity = Column(Integer, nullable=False)

    order_id = Column(Integer, ForeignKey('order.id'), nullable=False)
    order = relationship(
        'Order',
        back_populates='order_products',
        cascade='save-update, merge'
    )

    product_id = Column(Integer, ForeignKey('product.id'), nullable=False)
    product = relationship(
        'Product',
        back_populates='order_products',
        cascade='save-update, merge'
    )

    __table_args__ = (
        UniqueConstraint('order_id', 'product_id'),
    )

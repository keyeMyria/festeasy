from sqlalchemy import Column, Integer, Numeric, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

from backend import db
from backend.models.utils import Entity


class InvoiceProduct(db.Model, Entity):
    def __repr__(self):
        return '<InvoiceProduct {self.id}>'.format(self=self)

    unit_price_rands = Column(Numeric, nullable=False)
    quantity = Column(Integer, nullable=False)

    product_id = Column(ForeignKey('product.id'), nullable=False)
    product = relationship('Product', back_populates='invoice_products')

    invoice_id = Column(ForeignKey('invoice.id'), nullable=False)
    invoice = relationship('Invoice', back_populates='invoice_products')

    @property
    def sub_total_rands(self):
        return self.quantity * self.unit_price_rands

    __table_args__ = (
        UniqueConstraint('invoice_id', 'product_id'),
    )

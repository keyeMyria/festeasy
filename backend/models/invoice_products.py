from sqlalchemy import Column, Integer, Numeric
from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship, column_property

from backend import db
from backend.models import Entity


class InvoiceProduct(db.Model, Entity):
    __tablename__ = 'invoice_product'

    def __repr__(self):
        return '<InvoiceProduct {id}>'.format(id=self.id)

    unit_price_rands = Column(Numeric, nullable=False)

    product_id = Column(Integer, ForeignKey('product.id'), nullable=False)
    product = relationship('Product', back_populates='invoice_products')

    invoice_id = Column(Integer, ForeignKey('invoice.id'), nullable=False)
    invoice = relationship('Invoice', back_populates='invoice_products')

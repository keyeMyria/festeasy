from sqlalchemy import Column, Integer, Numeric
from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship, column_property

from backend import db
from backend.models import Entity, Dumpable


class InvoiceProduct(db.Model, Entity, Dumpable):
    __tablename__ = 'invoice_product'

    whitelist = [
        'id',
        'created_on',
        'sub_total_rands',
        'unit_price_rands',
        'quantity',
        'product',
    ]

    def __init__(self, unit_price_rands=None, 
            quantity=None, product=None, invoice=None):
        self.unit_price_rands = unit_price_rands
        self.quantity = quantity
        self.product = product
        self.invoice = invoice

    def __repr__(self):
        return '<InvoiceProduct {id}>'.format(id=self.id)

    unit_price_rands = Column(Numeric, nullable=False)
    quantity = Column(Integer, default=1, nullable=False)

    product_id = Column(Integer, ForeignKey('product.id'), nullable=False)
    product = relationship('Product', back_populates='invoice_products')

    invoice_id = Column(Integer, ForeignKey('invoice.id'), nullable=False)
    invoice = relationship('Invoice', back_populates='invoice_products')

    sub_total_rands = column_property(
        unit_price_rands * quantity
        )

    __table_args__ = (
        UniqueConstraint('invoice_id', 'product_id'),
    )

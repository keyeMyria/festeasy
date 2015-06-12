import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy import ForeignKey, func, select
from sqlalchemy.orm import relationship, column_property

from backend import db
from backend.models import Entity, Dumpable, InvoiceProduct


class Invoice(db.Model, Entity, Dumpable):
    __tablename__ = 'invoice'

    whitelist = [
        'id',
        'created_on',
        'total_rands',
    ]

    order_id = Column(Integer, ForeignKey('order.id'), nullable=False)
    order = relationship('Order', back_populates='invoices')

    products = relationship('Product', secondary='invoice_product', back_populates='invoices')
    invoice_products = relationship('InvoiceProduct', back_populates='invoice')

    def __init__(self, order=None, invoice_products=[], products=[]):
        self.order = order
        self.invoice_products = invoice_products
        self.products = products

    def from_order(self, order):
        with db.session.no_autoflush:
            self.order = order
            for order_product in order.order_products:
                self.invoice_products.append(InvoiceProduct(
                    product=order_product.product,
                    unit_price_rands=order_product.unit_price_rands,
                    quantity=order_product.quantity,
                    invoice=self,
                    ))

    def __repr__(self):
        return '<Invoice {id}>'.format(id=self.id)

Invoice.total_rands = column_property(
    select([func.sum(InvoiceProduct.sub_total_rands)]).where(InvoiceProduct.invoice_id==Invoice.id).correlate(Invoice)
    )

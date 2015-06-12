import datetime
from sqlalchemy import Column, Integer, String, DateTime, Numeric
from sqlalchemy import ForeignKey, func, select, cast
from sqlalchemy.orm import relationship, column_property

from backend import db
from backend.models import Entity, Dumpable, InvoiceProduct
from backend.models import Payment


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

    payments = relationship('Payment', back_populates='invoice')

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

# Total amount for an Invoice
Invoice.total_rands = column_property(
    select([func.sum(InvoiceProduct.sub_total_rands)]).where(InvoiceProduct.invoice_id==Invoice.id).correlate(Invoice)
    )

# Total amount which needs to be paid.
Invoice.amount_due_rands = column_property(
    cast(Invoice.total_rands - select([func.sum(Payment.amount_rands)]).where(Payment.invoice_id==Invoice.id).correlate(Invoice), Numeric)
    )

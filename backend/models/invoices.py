from sqlalchemy import Column, Integer
from sqlalchemy import ForeignKey, func, select
from sqlalchemy.orm import relationship, column_property

from backend import db

from . import Payment, OrderProduct, InvoiceProduct
from .utils import Entity


class Invoice(db.Model, Entity):
    __tablename__ = 'invoice'

    # TODO: Imporve testing
    @staticmethod
    def from_order(order):
        if not order.order_products:
            raise Exception('Order has not products.')
        invoice = Invoice()
        invoice.order = order
        order_products = (
            OrderProduct.query
            .filter(OrderProduct.order == order)
            .all()
        )
        for order_product in order_products:
            invoice.invoice_products.append(
                InvoiceProduct(
                    product=order_product.product,
                    unit_price_rands=order_product.unit_price_rands,
                    invoice=invoice,
                )
            )
        return invoice

    def __repr__(self):
        return '<Invoice {id}>'.format(id=self.id)

    order_id = Column(
        Integer,
        ForeignKey('order.id'),
        nullable=False
    )
    order = relationship(
        'Order',
        back_populates='invoices'
    )

    products = relationship(
        'Product',
        secondary='invoice_product',
        back_populates='invoices'
    )
    invoice_products = relationship(
        'InvoiceProduct',
        back_populates='invoice'
    )

    payments = relationship(
        'Payment',
        back_populates='invoice'
    )

# Total amount for an Invoice
Invoice.total_rands = column_property(
    select([func.sum(InvoiceProduct.unit_price_rands)]).where(
        InvoiceProduct.invoice_id == Invoice.id).correlate(Invoice)
)

# Total amount which needs to be paid.
Invoice.amount_due_rands = column_property(
    Invoice.total_rands - select(
        [func.coalesce(func.sum(Payment.amount_rands), 0)]
    ).where(Payment.invoice_id == Invoice.id).correlate(Invoice)
)

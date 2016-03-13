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
            raise Exception('Order has no products.')
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
                    quantity=order_product.quantity,
                    invoice=invoice,
                )
            )
        return invoice

    @property
    def total_rands(self):
        total = 0
        for ip in self.invoice_products:
            total += ip.sub_total_rands
        return total

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

    invoice_products = relationship(
        'InvoiceProduct',
        back_populates='invoice'
    )

    payments = relationship(
        'Payment',
        back_populates='invoice'
    )

    @property
    def payments_total_rands(self):
        total = 0
        for p in self.payments:
            total += p.amount_rands
        return total

    @property
    def amount_due_rands(self):
        return self.total_rands - self.payments_total_rands

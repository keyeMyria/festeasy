from sqlalchemy import Column, Integer
from sqlalchemy import ForeignKey, func, select
from sqlalchemy.orm import relationship, column_property

from backend import db
from backend.models import Entity, InvoiceProduct
from backend.models import Payment, OrderProduct


class Invoice(db.Model, Entity):
    __tablename__ = 'invoice'

    # TODO: Imporve testing
    @staticmethod
    def from_order(order):
        if not order.order_products:
            raise Exception('Order has not products.')
        invoice = Invoice()
        invoice.order = order
        things = (db.session.query(
            OrderProduct, func.count(OrderProduct.product_id))
            .filter(OrderProduct.order == order)
            .group_by(OrderProduct.product_id)
            .all())
        for order_product, quantity in things:
            invoice.invoice_products.append(
                InvoiceProduct(
                    product=order_product.product,
                    unit_price_rands=order_product.unit_price_rands,
                    quantity=quantity,
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
    select([func.sum(InvoiceProduct.sub_total_rands)]).where(
        InvoiceProduct.invoice_id == Invoice.id).correlate(Invoice)
)

# Total amount which needs to be paid.
Invoice.amount_due_rands = column_property(
    Invoice.total_rands - select(
        [func.coalesce(func.sum(Payment.amount_rands), 0)]
    ).where(Payment.invoice_id == Invoice.id).correlate(Invoice)
)

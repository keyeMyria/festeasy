from sqlalchemy import Column, Integer, Numeric
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from backend import db

from .utils import Entity


class Payment(db.Model, Entity):
    __tablename__ = 'payment'

    def __init__(self, invoice=None, amount_rands=None):
        self.invoice = invoice
        self.amount_rands = amount_rands

    def __repr__(self):
        return '<Payment {id}>'.format(id=self.id)

    invoice_id = Column(Integer, ForeignKey('invoice.id'), nullable=False)
    invoice = relationship('Invoice', back_populates='payments')

    payu_transactions = relationship(
        'PayUTransaction',
        back_populates='payment',
    )

    # Amount paid in Rands.
    amount_rands = Column(Numeric, nullable=False)

from sqlalchemy import Column, Numeric, ForeignKey
from sqlalchemy.orm import relationship

from backend import db

from .utils import Entity


class Payment(db.Model, Entity):
    def __repr__(self):
        return '<Payment {self.id}>'.format(self=self)

    # Amount paid in Rands.
    amount_rands = Column(Numeric, nullable=False)

    invoice_id = Column(ForeignKey('invoice.id'), nullable=False)
    invoice = relationship('Invoice', back_populates='payments')

    payu_transactions = relationship(
        'PayUTransaction',
        back_populates='payment',
    )

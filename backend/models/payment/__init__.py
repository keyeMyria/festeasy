import datetime
from sqlalchemy import Column, Integer, String, DateTime, Numeric
from sqlalchemy import ForeignKey, func, select
from sqlalchemy.orm import relationship, column_property

from backend import db
from backend.models import Entity, Dumpable


class Payment(db.Model, Entity, Dumpable):
    __tablename__ = 'payment'

    whitelist = [
        'id',
        'created_on',
        'amount_rands',
    ]

    invoice_id = Column(Integer, ForeignKey('invoice.id'), nullable=False)
    invoice = relationship('Invoice', back_populates='payments')

    # Amount paid in Rands.
    amount_rands = Column(Numeric, nullable=False)

    def __init__(self, invoice=None, amount_rands=None):
        self.invoice = invoice
        self.amount_rands = amount_rands

    def __repr__(self):
        return '<Payment {id}>'.format(id=self.id)

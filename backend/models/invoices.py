import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from backend import db
from backend.models import Entity, Dumpable


class Invoice(db.Model, Entity, Dumpable):
    __tablename__ = 'invoice'

    whitelist = [
        'id',
        'created_on',
    ]

    order_id = Column(Integer, ForeignKey('order.id'), nullable=False)
    order = relationship('Order', back_populates='invoices')

    products = relationship('Product', secondary='invoice_product', back_populates='invoices')
    invoice_products = relationship('InvoiceProduct', back_populates='invoice')

    def __init__(self):
        pass

    def __repr__(self):
        return '<Invoice {id}>'.format(id=self.id)

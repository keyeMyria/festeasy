from sqlalchemy import Column, String, ForeignKey, Boolean, BigInteger, Integer
from sqlalchemy.orm import relationship

from backend import db

from .utils import Entity


class PayUTransaction(db.Model, Entity):
    def __repr__(self):
        return '<PayUTransaction {self.id}>'.format(self=self)

    payu_reference = Column(BigInteger, unique=True, nullable=False)
    merchant_reference = Column(Integer)
    successful = Column(Boolean)
    result_message = Column(String)
    result_code = Column(String)
    display_message = Column(String)
    point_of_failure = Column(String)

    invoice_id = Column(ForeignKey('invoice.id'), nullable=False)
    invoice = relationship(
        'Invoice',
        back_populates='payu_transactions',
    )

    payment_id = Column(ForeignKey('payment.id'))
    payment = relationship(
        'Payment',
        back_populates='payu_transactions',
    )

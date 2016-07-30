from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from backend import db

from .utils import Entity


class Collection(db.Model, Entity):

    def __repr__(self):
        return '<Collection {id}>'.format(id=self.id)

    order_id = Column(Integer, ForeignKey('order.id'), nullable=False)
    order = relationship(
        'Order',
        back_populates='collection',
        uselist=False,
    )

from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship

from backend import db
from backend.models.utils import Entity


class Collection(db.Model, Entity):
    def __repr__(self):
        return '<Collection {self.id}>'.format(self=self)

    order_id = Column(ForeignKey('order.id'), nullable=False)
    order = relationship(
        'Order',
        back_populates='collection',
        uselist=False,
    )

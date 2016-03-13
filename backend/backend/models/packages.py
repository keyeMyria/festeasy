from sqlalchemy import Column, Integer
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from backend import db

from .utils import Entity


class Package(db.Model, Entity):

    def __repr__(self):
        return '<Package {id}>'.format(id=self.id)

    order_id = Column(Integer, ForeignKey('order.id'), nullable=False)
    order = relationship(
        'Order',
        back_populates='packages',
    )

    packaged_stock_units = relationship(
        'PackagedStockUnit',
        back_populates='package',
        cascade='save-update, merge, delete, delete-orphan'
    )

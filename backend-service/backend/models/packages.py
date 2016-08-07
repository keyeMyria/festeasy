from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship

from backend import db

from .utils import Entity


class Package(db.Model, Entity):
    def __repr__(self):
        return '<Package {self.id}>'.format(self=self)

    order_id = Column(ForeignKey('order.id'), nullable=False)
    order = relationship(
        'Order',
        back_populates='packages',
    )

    packaged_stock_units = relationship(
        'PackagedStockUnit',
        back_populates='package',
        cascade='save-update, merge, delete, delete-orphan'
    )

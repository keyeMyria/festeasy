from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship

from backend import db

from .utils import Entity


class PackagedStockUnit(db.Model, Entity):
    def __repr__(self):
        return '<PackagedStockUnit {self.id}>'.format(self=self)

    stock_unit_id = Column(
        ForeignKey('stock_unit.id'),
        nullable=False,
        unique=True,
    )
    stock_unit = relationship(
        'StockUnit',
        back_populates='packaged_stock_unit',
        uselist=False,
    )

    package_id = Column(ForeignKey('package.id'), nullable=False)
    package = relationship(
        'Package',
        back_populates='packaged_stock_units',
    )

from sqlalchemy import Column, Integer, Numeric
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from backend import db

from .utils import Entity


class PackagedStockUnit(db.Model, Entity):

    def __repr__(self):
        return '<PackagedStockUnit {id}>'.format(id=self.id)

    stock_unit_id = Column(Integer, ForeignKey('stock_unit.id'), nullable=False)
    stock_unit = relationship(
        'StockUnit',
        back_populates='packaged_stock_unit',
        uselist=False,
    )

    package_id = Column(Integer, ForeignKey('package.id'), nullable=False)
    package = relationship(
        'Package',
        back_populates='packaged_stock_units',
    )

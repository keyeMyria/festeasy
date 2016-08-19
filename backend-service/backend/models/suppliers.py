from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from backend import db

from .utils import Entity


class Supplier(db.Model, Entity):
    """A supplier is a physical store from where Products
    are bought.
    EG: Woolies in Palmyra Junction.
    """

    def __repr__(self):
        return '<Supplier {self.id}>'.format(sef=self)

    name = Column(String)
    location = Column(String)
    contact_numer = Column(String)

    stock_units = relationship(
        'StockUnit',
        back_populates='supplier',
    )

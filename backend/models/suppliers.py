from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

from backend import db
from backend.models import Entity


class Supplier(db.Model, Entity):
    """
    A supplier is a physical store from where Products
    are bought.
    EG: Woolies in Palmyra Junction.
    """
    __tablename__ = 'supplier'

    name = Column(String)
    location = Column(String)
    contact_numer = Column(String)

    base_supplier_id = Column(
        Integer,
        ForeignKey('base_supplier.id'),
        )
    base_supplier = relationship(
        'BaseSupplier',
        back_populates="suppliers",
    )

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from backend import db

from .utils import Entity


class BaseSupplier(db.Model, Entity):
    """
    A BaseSupplier is a chain/company/parent company.
    EG: Woolies.
    """
    __tablename__ = 'base_supplier'

    def __repr__(self):
        return '<BaseSupplier {id}>'.format(id=self.id)

    name = Column(String)

    suppliers = relationship(
        'Supplier',
        back_populates='base_supplier'
    )

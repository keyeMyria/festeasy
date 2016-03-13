from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from backend import db

from .utils import Entity


class Category(db.Model, Entity):
    __tablename__ = 'category'

    name = Column(String)
    description = Column(String)

    def __repr__(self):
        return '<Category {id}>'.format(id=self.id)

    product_categories = relationship(
        'ProductCategory',
        back_populates='category'
    )

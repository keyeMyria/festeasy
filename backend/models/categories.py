from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey, UniqueConstraint, select
from sqlalchemy.orm import relationship, column_property

from backend import db
from backend.models import Entity


class Category(db.Model, Entity):
    __tablename__ = 'category'

    name = Column(String)
    description = Column(String)

    def __repr__(self):
        return '<Category {id}>'.format(id=self.id)

    products = relationship(
        'Product',
        secondary='product_category',
        back_populates='categories',
    )

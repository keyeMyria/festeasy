from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey, UniqueConstraint, select
from sqlalchemy.orm import relationship, column_property

from backend import db
from backend.models import Entity


class ProductCategory(db.Model, Entity):
    __tablename__ = 'product_category'

    def __repr__(self):
        return '<ProductCategory {id}>'.format(id=self.id)

    product_id = Column(Integer, ForeignKey('product.id'), nullable=False)
    category_id = Column(Integer, ForeignKey('category.id'), nullable=False)

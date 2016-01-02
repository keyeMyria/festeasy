from sqlalchemy import Column, Integer
from sqlalchemy import ForeignKey

from backend import db

from .utils import Entity


class ProductCategory(db.Model, Entity):
    """
    Represents a Product belonging to a Category.
    """
    __tablename__ = 'product_category'

    def __repr__(self):
        return '<ProductCategory {id}>'.format(id=self.id)

    product_id = Column(Integer, ForeignKey('product.id'), nullable=False)
    category_id = Column(Integer, ForeignKey('category.id'), nullable=False)

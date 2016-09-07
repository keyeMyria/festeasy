from sqlalchemy import Column, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

from backend import db

from .utils import Entity


class ProductCategory(db.Model, Entity):
    """Represents a Product belonging to a Category.
    """
    def __repr__(self):
        return '<ProductCategory {self.id}>'.format(self=self)

    product_id = Column(ForeignKey('product.id'), nullable=False)
    product = relationship(
        'Product',
        back_populates='product_categories',
    )

    category_id = Column(ForeignKey('category.id'), nullable=False)
    category = relationship(
        'Category',
        back_populates='product_categories',
    )

    __table_args__ = (
        UniqueConstraint('product_id', 'category_id'),
    )

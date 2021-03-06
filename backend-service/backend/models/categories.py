from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from backend import db
from backend.models.utils import Entity


class Category(db.Model, Entity):
    def __repr__(self):
        return '<Category {self.id}>'.format(self=self)

    name = Column(String)
    description = Column(String)

    product_categories = relationship(
        'ProductCategory',
        back_populates='category'
    )

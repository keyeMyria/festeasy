from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from backend import db
from backend.models.utils import Entity


class Group(db.Model, Entity):
    def __repr__(self):
        return '<Group {self.id}>'.format(self=self)

    name = Column(String)
    description = Column(String)

    categories = relationship(
        'Category',
        back_populates='group'
    )

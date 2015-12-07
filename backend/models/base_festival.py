from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from backend import db
from backend.models import Entity


class BaseFestival(db.Model, Entity):
    __tablename__ = 'base_festival'

    def __repr__(self):
        return '<BaseFestival {id}>'.format(id=self.id)

    name = Column(String)
    description = Column(String)

    festivals = relationship(
        'Festival',
        back_populates='base_festival',
    )

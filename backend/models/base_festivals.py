from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from backend import db
from .utils import Entity


class BaseFestival(db.Model, Entity):
    """
    A BaseFestival represents the idea of a
    group of festivals which may occur on a regular basis.
    EG: Rocking The Diases, as apposed to Rocking The Diases 2015.
    """
    __tablename__ = 'base_festival'

    def __repr__(self):
        return '<BaseFestival {id}>'.format(id=self.id)

    name = Column(String)
    description = Column(String)

    festivals = relationship(
        'Festival',
        back_populates='base_festival',
    )

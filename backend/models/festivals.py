from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from backend import db

from .utils import Entity


class Festival(db.Model, Entity):
    __tablename__ = 'festival'

    def __repr__(self):
        return '<Festival {id}>'.format(id=self.id)

    name = Column(String, nullable=False)
    starts_on = Column(DateTime, nullable=False)
    ends_on = Column(DateTime)
    description = Column(String)
    website_link = Column(String)
    ticket_link = Column(String)
    facebook_link = Column(String)

    base_festival_id = Column(
        Integer,
        ForeignKey('base_festival.id'),
        nullable=False,
    )
    base_festival = relationship(
        'BaseFestival',
        back_populates='festivals',
        cascade='save-update, merge, delete'
    )

    orders = relationship(
        'Order',
        back_populates='festival',
        cascade='save-update, merge'
    )
    carts = relationship(
        'Cart',
        back_populates='festival',
    )

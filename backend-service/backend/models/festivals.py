from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import relationship

from backend import db
from backend.models.utils import Entity


class Festival(db.Model, Entity):
    def __repr__(self):
        return '<Festival {self.id}>'.format(self=self)

    name = Column(String, nullable=False)
    starts_on = Column(DateTime, nullable=False)
    ends_on = Column(DateTime)
    description = Column(String)
    website_link = Column(String)
    ticket_link = Column(String)
    facebook_link = Column(String)

    orders = relationship(
        'Order',
        back_populates='festival',
    )

    carts = relationship(
        'Cart',
        back_populates='festival',
    )

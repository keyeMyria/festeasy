from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import relationship

from backend import db
from backend.models import Entity


class Festival(db.Model, Entity):
    __tablename__ = 'festival'

    def __repr__(self):
        return '<Festival {id}>'.format(id=self.id)

    name = Column(String(150), nullable=False)
    starts_on = Column(DateTime)
    ends_on = Column(DateTime)
    description = Column(String)
    website_link = Column(String)
    ticket_link = Column(String)
    facebook_link = Column(String)

    orders = relationship(
        'Order',
        back_populates='festival',
        cascade='save-update, merge'
    )
    carts = relationship('Cart', back_populates='festival')

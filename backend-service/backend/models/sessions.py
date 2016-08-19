from datetime import datetime, timedelta
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from backend import db

from .utils import Entity


class Session(db.Model, Entity):
    def __init__(self, user=None, expires_on=None, token=None):
        self.expires_on = (expires_on if expires_on
                           else datetime.utcnow() + timedelta(days=30))
        # TODO: Fix import dependency issue.
        from backend.utils import random_string
        self.token = token if token else random_string(32)
        self.user = user

    def __repr__(self):
        return '<Session {self.id}>'.format(self=self)

    expires_on = Column(DateTime, nullable=False)
    token = Column(String(200), nullable=False, unique=True)

    user_id = Column(ForeignKey('user.id'), nullable=False)
    user = relationship(
        'User',
        back_populates='sessions',
    )

    def is_valid(self):
        now = datetime.now()
        return self.expires_on > now

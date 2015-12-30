import datetime
import jwt
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from backend import db
from backend.models import Entity


class Session(db.Model, Entity):
    __tablename__ = 'session'

    def generate_token(self):
        assert self.user.id is not None
        payload = {
            'sub': self.user.id,
            'iat': self.created_on,
            'exp': self.expires_on,
        }
        self.token = jwt.encode(payload, 'secret').decode('unicode_escape')

    def __repr__(self):
        return '<Session {id}>'.format(id=self.id)

    expires_on = Column(DateTime, nullable=False)
    token = Column(String(200), nullable=False, unique=True)

    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship(
        'User',
        back_populates='sessions',
        cascade='save-update, merge',
    )

    def is_valid(self):
        now = datetime.datetime.utcnow()
        return self.expires_on > now

import datetime
from uuid import uuid4
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from backend import db
from backend.models.utils import Entity


class ForgotPasswordToken(db.Model, Entity):
    def __repr__(self):
        return '<ForgotPasswordToken id={self.id}'.format(self=self)

    token = Column(String, unique=True, nullable=False)
    expires_on = Column(DateTime, nullable=False)
    used_on = Column(DateTime)

    user_id = Column(ForeignKey('user.id'), nullable=False)
    user = relationship(
        'User',
        back_populates='forgot_password_tokens'
    )

    def is_valid(self):
        now = datetime.datetime.now()
        return self.expires_on > now and not self.used_on

    @staticmethod
    def create_for_user(user):
        now = datetime.datetime.now()
        token = str(uuid4())
        expires_on = now + datetime.timedelta(days=7)
        return ForgotPasswordToken(
            expires_on=expires_on,
            token=token,
            user=user,
        )

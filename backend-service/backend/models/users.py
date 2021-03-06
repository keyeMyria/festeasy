import datetime
from sqlalchemy import Column, String, Boolean, ForeignKey, CheckConstraint, \
    or_, and_
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

from backend import db

from . import Session
from .utils import Entity


class User(db.Model, Entity):
    def __init__(self, password=None, **kwargs):
        super().__init__(**kwargs)
        if password:
            self.set_password(password)

    def __repr__(self):
        return '<User {self.id}>'.format(self=self)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def has_password(self, password):
        return check_password_hash(self.password_hash, password)

    def invalidate_active_sessions(self):
        now = datetime.datetime.now()
        active_sessions = (
            Session.query
            .filter(Session.user_id == self.id)
            .filter(Session.expires_on >= now)
            .all())
        for active_session in active_sessions:
            active_session.expires_on = now
            db.session.add(active_session)
        db.session.commit()

    email_address = Column(String(200), unique=True)
    password_hash = Column(String(200))
    guest_token = Column(String(200), unique=True)
    first_name = Column(String(100), nullable=True)
    last_name = Column(String(100))
    is_admin = Column(Boolean, default=False, nullable=False)
    facebook = Column(String)

    sessions = relationship(
        'Session',
        back_populates='user',
        cascade='save-update, merge, delete, delete-orphan',
    )

    orders = relationship(
        'Order',
        back_populates='user',
        cascade='save-update, merge, delete, delete-orphan',
    )

    cart_id = Column(
        ForeignKey('cart.id'),
        nullable=False,
    )
    cart = relationship(
        'Cart',
        back_populates='user',
        uselist=False,
        cascade='save-update, merge, delete',
    )

    forgot_password_tokens = relationship(
        'ForgotPasswordToken',
        back_populates='user',
    )

    __table_args__ = (
        CheckConstraint(
            or_(
                facebook != None,
                guest_token != None,
                and_(
                    password_hash != None, email_address != None,
                    first_name != None
                )
            )
        ),
    )

    @property
    def is_guest(self):
        return (self.guest_token and not any([
            self.email_address,
            self.password_hash,
            self.first_name,
            ])
        )

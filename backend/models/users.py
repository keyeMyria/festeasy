import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

from backend import db
from backend.models import Entity, Dumpable


class User(db.Model, Entity, Dumpable):
    __tablename__ = 'user'

    whitelist = [
        'id',
        'created_on',
        'email_address',
        'user_cart_products',
        'current_cart_event',
    ]
    
    email_address = Column(String(200), unique=True, nullable=False)
    password_hash = Column(String(200), unique=True, nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100))

    sessions = relationship('Session', back_populates='user', 
        cascade='save-update, merge, delete, delete-orphan')

    cart_products = relationship('Product', secondary='user_cart_product',
        cascade='save-update, merge')

    user_cart_products = relationship('UserCartProduct',
        cascade='save-update, merge, delete, delete-orphan')

    current_cart_event = relationship('Event', back_populates='users')
    current_cart_event_id = Column(Integer, ForeignKey('event.id'), nullable=True)

    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        db.session.add(self)
        db.session.commit()
        db.session.close()

    def has_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __init__(self, email_address, password, first_name):
        self.email_address = email_address
        self.password_hash = generate_password_hash(password)
        self.first_name = first_name

    def __repr__(self):
        return '<User {id}>'.format(id=self.id)

import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import ForeignKey, CheckConstraint
from sqlalchemy import or_, and_
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
        'first_name',
        'last_name',
    ]
    
    email_address = Column(String(200), unique=True, nullable=True)
    password_hash = Column(String(200), nullable=True)
    guest_token = Column(String(200), unique=True, nullable=True)
    first_name = Column(String(100), nullable=True)
    last_name = Column(String(100))

    sessions = relationship('Session', back_populates='user', 
        cascade='save-update, merge, delete, delete-orphan')

    orders = relationship('Order', back_populates='user',
        cascade='save-update, merge, delete, delete-orphan')

    cart_id = Column(Integer, ForeignKey('cart.id'), nullable=False)
    cart = relationship('Cart', back_populates='user', uselist=False,
        cascade='save-update, merge, delete')

    __table_args__ = (
        CheckConstraint(
            or_(
                guest_token != None, 
                and_(password_hash != None, email_address != None, first_name != None))
            ),
    )
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def has_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __init__(self, email_address=None, password=None, first_name=None, last_name=None, cart=None,
        sessions=[], orders=[]):
        self.email_address = email_address
        if password:
            self.password_hash = generate_password_hash(password)
        self.first_name = first_name
        self.last_name = last_name
        self.cart = cart
        self.sessions = sessions
        self.orders = orders

    def __repr__(self):
        return '<User {id}>'.format(id=self.id)

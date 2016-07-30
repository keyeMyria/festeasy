import datetime

from factory import Factory, SubFactory

from backend.models import Session
from . import UserFactory


class SessionFactory(Factory):
    class Meta:
        model = Session

    user = SubFactory(UserFactory)
    expires_on = datetime.datetime.now()
    token = 'asdf'

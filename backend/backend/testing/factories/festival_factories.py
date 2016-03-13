import datetime
from factory import Factory, SubFactory

from backend.models import Festival
from . import BaseFestivalFactory


class FestivalFactory(Factory):
    class Meta:
        model = Festival

    starts_on = datetime.datetime.now()
    ends_on = datetime.datetime.now() + datetime.timedelta(days=2)
    name = 'The Test Festival'
    description = 'This is a description.'
    base_festival = SubFactory(BaseFestivalFactory)

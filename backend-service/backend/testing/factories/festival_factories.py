import datetime
from factory import Factory

from backend.models import Festival


class FestivalFactory(Factory):
    class Meta:
        model = Festival

    starts_on = datetime.datetime.now()
    ends_on = datetime.datetime.now() + datetime.timedelta(days=2)
    name = 'The Test Festival'
    description = 'This is a description.'

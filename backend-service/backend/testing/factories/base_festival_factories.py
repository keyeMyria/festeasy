from factory import Factory

from backend.models import BaseFestival


class BaseFestivalFactory(Factory):
    class Meta:
        model = BaseFestival

    name = 'A Base Festival'
    description = 'Some description.'

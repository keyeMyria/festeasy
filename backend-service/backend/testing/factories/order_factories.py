from factory import Factory, SubFactory

from backend.models import Order
from . import FestivalFactory, UserFactory


class OrderFactory(Factory):
    class Meta:
        model = Order

    festival = SubFactory(FestivalFactory)
    user = SubFactory(UserFactory)

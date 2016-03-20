from factory import Factory, SubFactory

from backend.models import Collection

from .order_factories import OrderFactory


class CollectionFactory(Factory):
    class Meta:
        model = Collection

    order = SubFactory(OrderFactory)

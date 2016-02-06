from factory import Factory, SubFactory

from backend.models import Package

from . import OrderFactory


class PackageFactory(Factory):
    class Meta:
        model = Package

    order = SubFactory(OrderFactory)

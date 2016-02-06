from factory import Factory, SubFactory

from backend.models import PackagedStockUnit

from . import PackageFactory, StockUnitFactory


class PackagedStockUnitFactory(Factory):
    class Meta:
        model = PackagedStockUnit

    package = SubFactory(PackageFactory)
    stock_unit = SubFactory(StockUnitFactory)

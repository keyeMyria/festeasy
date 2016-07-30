from backend.api.v1 import v1_api
from .packaged_stock_unit_collection import PackagedStockUnitCollection
from .packaged_stock_unit_singleton import PackagedStockUnitSingleton


v1_api.add_resource(PackagedStockUnitCollection,
                    '/packaged-stock-units')

v1_api.add_resource(PackagedStockUnitSingleton,
                    '/packaged-stock-units/<int:packaged_stock_unit_id>')

from backend.api.v1 import v1_api
from .packaged_stock_unit_collection import PackagedStockUnitCollection


v1_api.add_resource(PackagedStockUnitCollection,
                    '/packaged-stock-units')

from backend.api.v1 import v1_api
from .supplier_collection import SupplierCollection


v1_api.add_resource(SupplierCollection,
                    '/suppliers')

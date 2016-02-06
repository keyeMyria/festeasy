from backend.api.v1 import v1_api
from .package_collection import PackageCollection


v1_api.add_resource(PackageCollection,
                    '/packages')

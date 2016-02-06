from backend.api.v1 import v1_api
from .package_collection import PackageCollection
from .package_singleton import PackageSingleton


v1_api.add_resource(PackageCollection,
                    '/packages')

v1_api.add_resource(PackageSingleton,
                    '/packages/<int:package_id>')

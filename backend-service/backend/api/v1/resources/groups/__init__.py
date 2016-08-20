from backend.api.v1 import v1_api
from .group_collection import GroupCollection

v1_api.add_resource(GroupCollection,
                    '/groups')

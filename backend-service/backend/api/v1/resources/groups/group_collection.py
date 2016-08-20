from flask_restful import Resource

from backend.models import Group
from backend.api.v1.schemas import GroupSchema


group_schema = GroupSchema()


class GroupCollection(Resource):
    def get(self):
        groups = Group.query.all()
        return group_schema.dump(groups, many=True).data

from flask import Response
from flask.json import JSONEncoder


class CustomJSONEncoder(JSONEncoder):
    """A JSON encoder which knows how to dump dumpable models.
    """
    def default(self, obj):
        from backend import models
        if isinstance(obj, models.Dumpable):
            return obj.dump()
        return JSONEncoder.default(self, obj)

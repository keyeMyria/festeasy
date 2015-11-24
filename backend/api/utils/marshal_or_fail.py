import logging

logger = logging.getLogger(__name__)


def marshal_or_fail(method, data, schema, many=False):
    assert method in ['dump', 'load']
    if not many and type(data) == list:
        logger.warn("Passed in data is a list and 'many' is not True.")
    f = getattr(schema, method)
    data, errors = f(data, many=many)
    if errors:
        raise Exception("Errors occured")
    return data

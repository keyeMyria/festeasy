def marshal_or_fail(method, data, schema, many=False):
    f = getattr(schema, method)
    data, errors = f(data, many=many)
    if errors:
        raise Exception("Errors occured")
    return data

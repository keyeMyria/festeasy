def marshal_or_fail(data, schema, many=False):
    schema = schema()
    data, errors = schema.dump(data, many=many)
    if errors:
        raise Exception("Errors occured")
    return data

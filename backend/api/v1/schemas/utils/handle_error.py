from backend.api.v1.exceptions import APIException


def handle_error(error, data):
    raise APIException(
        message='Somthing went wrong.',
        payload={
            'data': data,
            'errors': error.messages,
        },
    )

from flask import request
from functools import wraps

from backend.api.v1 import forms


def takes_form(form, form_name='form', mapping={}):
    """ Calls the decorated function the given form instantiated and fed the aruments of either request.json
    or the empty dict, updated with any uploaded files.

    Optionally also validates the form.
    """

    def decor(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            Form = getattr(forms, form)
            # Populating the form from flask like this is a bit of a hack, but so is wtforms :p
            data = request.form.to_dict() or request.json or request.args.to_dict() or dict()
            data = data.copy()
            data.update(request.files)

            mapped_data = dict()

            for k, v in data.items():
                if k in mapping:
                    mapped_data[mapping[k]] = v
                else:
                    mapped_data[k] = v

            form_instance = Form(**mapped_data)
            kwargs[form_name] = form_instance
            return f(*args, **kwargs)
        return decorated_function
    return decor

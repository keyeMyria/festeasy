

def template_entity(entity_template, kwargs):
    for key, val in entity_template.items():
        if key not in kwargs.keys():
            kwargs[key] = val
    return kwargs

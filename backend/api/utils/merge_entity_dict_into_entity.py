
# TODO: Test.
def merge_entity_dict_into_entity(allowed_attrs, entity_dict, entity):
	for key, val in entity_dict.items():
		if key in allowed_attrs:
			setattr(entity, key, val)
	return entity

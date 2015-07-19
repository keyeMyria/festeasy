
# TODO: Test.
def merge_entity_dict_into_entity(allowed_attrs, entity_dict, entity):
	for key, val in entity_dict.iteritems():
		if key in allowed_attrs:
			setattr(entity, key, val)
	return entity


# TODO: Test.
def merge_entity_dict_into_entity(allowed_attrs, entity_dict, entity):
	for key, val in entity_dict.iteritems():
		if key in allowed_attrs:
			setattr(entity, key, val)
		else:
			if key != 'id':
				raise Exception("entity_dict contained a key which was not in allowed_attrs and is not ID.")
	return entity

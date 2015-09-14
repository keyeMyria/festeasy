auth.factory('authService', () ->
	service = {}
	service.user = null
	service.session = null

	return service
)
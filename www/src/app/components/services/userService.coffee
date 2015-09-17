services.factory('userService', (Restangular) ->

	service = Restangular.service('users')
	return service
)

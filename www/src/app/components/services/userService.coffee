services.factory('userService', (Restangular) ->
	return Restangular.service('users')
)

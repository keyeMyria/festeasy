services.factory('packageService', (Restangular) ->
	return Restangular.service('packages')
)

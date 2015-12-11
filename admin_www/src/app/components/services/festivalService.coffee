services.factory('festivalService', (Restangular) ->
	return Restangular.service('festivals')
)

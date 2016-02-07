services.factory('psuService', (Restangular) ->
	return Restangular.service('packaged-stock-units')
)

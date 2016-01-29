services.factory('orderService', (Restangular) ->
	return Restangular.service('orders')
)

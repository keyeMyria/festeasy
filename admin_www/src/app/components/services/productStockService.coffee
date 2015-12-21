services.factory('productStockService', (Restangular) ->
	return Restangular.service('product-stocks')
)

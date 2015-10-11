services.factory('productService', (Restangular) ->
	return Restangular.service('products')
)

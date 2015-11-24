store.controller('storeController', ($scope, productService) ->
	getProducts = productService.getList()
	getProducts.then((response) ->
		$scope.products = response
	)
	getProducts.catch((response) ->
		$scope.error = true
	)
)

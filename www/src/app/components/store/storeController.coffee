store.controller('storeController', ($scope, productService, $stateParams) ->
	getProducts = productService.getList($stateParams)
	getProducts.then((response) ->
		$scope.products = response
	)
	getProducts.catch((response) ->
		$scope.error = true
	)
)

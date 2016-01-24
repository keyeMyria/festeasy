store.controller('productController', ($scope, productService, $stateParams) ->
	$scope.error = false
	productId = $stateParams.productId
	product = productService.one(productId)
	getProduct = product.get()
	getProduct.then((response) ->
		$scope.product = response
	)
	getProduct.catch((response) ->
		$scope.error = true
	)
)

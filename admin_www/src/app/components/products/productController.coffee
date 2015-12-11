products.controller('productController', ($scope, productService, $stateParams) ->
	productId = $stateParams.productId
	product = productService.one(productId)
	getProduct = product.get()
	getProduct.then((repsonse) ->
		$scope.product = repsonse
	)
)

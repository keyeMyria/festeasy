products.controller('productsController', ($scope, productService) ->
	getProducts = productService.getList()
	getProducts.then((repsonse) ->
		$scope.products = repsonse
	)
)

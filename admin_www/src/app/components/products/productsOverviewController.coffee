products.controller('productsOverviewController', ($scope, productService) ->
	getProducts = productService.getList()
	getProducts.then((repsonse) ->
		$scope.products = repsonse
	)
)

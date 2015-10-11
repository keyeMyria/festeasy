store.controller('storeController', ($scope, productService) ->
	promise = productService.getList()
	promise.then((response) ->
		$scope.products = response
	)
	promise.catch((response) ->
		$scope.error = true
	)
)

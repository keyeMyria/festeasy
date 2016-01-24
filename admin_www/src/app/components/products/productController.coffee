products.controller('productController', ($scope, productService, ngNotify, $stateParams) ->
	$scope.error = false
	productId = $stateParams.productId
	product = productService.one(productId)
	getProduct = product.get()
	getProduct.then((repsonse) ->
		$scope.product = repsonse
	)
	getProduct.catch((repsonse) ->
		$scope.error = true
	)

	$scope.updateProduct = (product) ->
		patchProduct = product.patch(product)
		patchProduct.then((repsonse) ->
			ngNotify.set('Successfully updated product.')
		)
		patchProduct.catch((repsonse) ->
			ngNotify.set('Failed to update product.', 'error')
		)
)

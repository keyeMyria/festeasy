products.controller('productController', ($scope, productService, ngNotify, $stateParams) ->
	productId = $stateParams.productId
	product = productService.one(productId)
	getProduct = product.get()
	getProduct.then((repsonse) ->
		$scope.product = repsonse
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
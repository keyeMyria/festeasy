products.controller('createProductController', ($scope, ngNotify, productService) ->
	$scope.createProduct = (product) ->
		postProduct = productService.post(product)
		postProduct.then((response) ->
			ngNotify.set('Sucessfully created product.')
		)
		postProduct.catch((response) ->
			ngNotify.set('Failed to create product.', 'error')
		)
)
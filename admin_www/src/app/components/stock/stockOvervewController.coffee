stock.controller('stockOverviewController', ($scope, supplierService, productService, productStockService, ngNotify) ->
	$scope.selectedSupplier = null
	$scope.selectedProduct = null
	$scope.costRands = null
	$scope.quantity = null

	getProductStocks = productStockService.getList()
	getProductStocks.then((response) ->
		$scope.productStocks = response
	)

	getSuppliers = supplierService.getList()
	getSuppliers.then((response) ->
		$scope.suppliers = response
	)

	getProducts = productService.getList()
	getProducts.then((response) ->
		$scope.products = response
	)

	$scope.updateSelectedSupplier = (supplier, something) ->
		$scope.selectedSupplier = supplier

	$scope.updateSelectedProduct = (product, something) ->
		$scope.selectedProduct = product

	$scope.createProductStock = () ->
		params = {
			product_id: $scope.selectedProduct.id,
			supplier_id: $scope.selectedSupplier.id,
			cost_rands: $scope.costRands
		}
		post = productStockService.post(params)
		post.then((response) ->
			ngNotify.set('Successfully created new stock product.')
		)
)

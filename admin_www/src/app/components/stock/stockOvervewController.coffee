stock.controller('stockOverviewController', (
		$scope, supplierService, productService, productStockService, ngNotify, $q) ->
	$scope.selectedSupplier = null
	$scope.selectedProduct = null
	$scope.costRands = null
	$scope.quantity = 1

	$scope.fetchProductStocks = () ->
		getProductStocks = productStockService.getList()
		getProductStocks.then((response) ->
			$scope.productStocks = response
		)

	$scope.fetchProductStocks()

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
		promises = []
		params = {
			product_id: $scope.selectedProduct.id,
			supplier_id: $scope.selectedSupplier.id,
			cost_rands: $scope.costRands
		}
		for i in [1..$scope.quantity]
			promises.push(
				productStockService.post(params)
			)
		post = $q.all(promises)
		post.then((response) ->
			ngNotify.set('Successfully created new stock products.')
		)
		post.finally((response) ->
			$scope.fetchProductStocks()
		)
)

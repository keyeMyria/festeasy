stock.controller('stockOverviewController', (
		$scope, supplierService, productService, stockUnitService, ngNotify, $q) ->
	$scope.error = false
	$scope.selectedSupplier = null
	$scope.selectedProduct = null
	$scope.costRands = null
	$scope.quantity = 1

	$scope.fetchStockUnits = () ->
		getStockUnits = stockUnitService.getList()
		getStockUnits.then((response) ->
			$scope.stockUnits = response
		)
		getStockUnits.catch((response) ->
			$scope.error = true
		)

	$scope.fetchStockUnits()

	getSuppliers = supplierService.getList()
	getSuppliers.then((response) ->
		$scope.suppliers = response
	)
	getSuppliers.catch((response) ->
		$scope.error = true
	)

	getProducts = productService.getList()
	getProducts.then((response) ->
		$scope.products = response
	)
	getProducts.catch((response) ->
		$scope.error = true
	)

	$scope.updateSelectedSupplier = (supplier, something) ->
		$scope.selectedSupplier = supplier

	$scope.updateSelectedProduct = (product, something) ->
		$scope.selectedProduct = product

	$scope.createStockUnit = () ->
		promises = []
		params = {
			product_id: $scope.selectedProduct.id,
			supplier_id: $scope.selectedSupplier.id,
			cost_rands: $scope.costRands
		}
		for i in [1..$scope.quantity]
			promises.push(
				stockUnitService.post(params)
			)
		post = $q.all(promises)
		post.then((response) ->
			ngNotify.set('Successfully created new stock products.')
		)
		post.finally((response) ->
			$scope.fetchStockUnits()
		)
)

store.controller('productsController', ($scope, $state, productService, $stateParams) ->
	$scope.searchTerm = $stateParams.search
	$scope.placeholder = 'Search '
	
	if $stateParams.category
		$scope.placeholder += $stateParams.category

	$scope.search = () ->
		$state.go('base.store.products', {search: $scope.searchTerm}, {}, {reload: true})

	queryParams = {
		search: $stateParams.search
		category: $stateParams.category
	}
	getProducts = productService.getList(queryParams)
	getProducts.then((response) ->
		$scope.products = response
	)
	getProducts.catch((response) ->
		$scope.error = true
	)
)

store.controller('storeController', ($scope, $state, productService, $stateParams) ->
	$scope.searchTerm = $stateParams.search
	$scope.placeholder = 'Search '
	if $stateParams.category
		$scope.placeholder += $stateParams.category

	$scope.search = () ->
		$state.go('base.store', {search: $scope.searchTerm}, {}, {reload: true})
		
	getProducts = productService.getList($stateParams)
	getProducts.then((response) ->
		$scope.products = response
	)
	getProducts.catch((response) ->
		$scope.error = true
	)
)

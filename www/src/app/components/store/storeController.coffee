store.controller('storeController', ($scope, categoryService, $stateParams) ->
	$scope.currentCategory = $stateParams.category
	getCategories = categoryService.getList()
	getCategories.then((response) ->
		$scope.categories = response
	)
)
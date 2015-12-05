store.controller('storeController', ($scope, categoryService, $stateParams) ->
	$scope.cat = $stateParams.category
	getCategories = categoryService.getList()
	getCategories.then((response) ->
		$scope.categories = response
	)
)
store.controller('storeController', ($scope, $rootScope, categoryService, $stateParams) ->
	$scope.currentCategory = $stateParams.category
	getCategories = categoryService.getList()
	getCategories.then((response) ->
		$rootScope.categories = response
	)
)

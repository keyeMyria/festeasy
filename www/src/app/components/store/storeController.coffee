store.controller('storeController', ($scope, $rootScope, categoryService, $stateParams) ->
	$scope.currentCategory = $stateParams.category
	getCategories = categoryService.getList()
	getCategories.then((response) ->
		# Storing categories on the rootScope to prevent flickering.
		$rootScope.categories = response
	)
	getCategories.catch((response) ->
		$scope.error = true
	)
)

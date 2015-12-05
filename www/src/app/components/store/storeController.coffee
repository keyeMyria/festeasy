store.controller('storeController', ($scope, categoryService) ->
	getCategories = categoryService.getList()
	getCategories.then((response) ->
		$scope.categories = response
	)
)
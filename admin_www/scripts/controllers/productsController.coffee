app.controller('ProductsController', (productsService, $scope, $state) ->

	productsService.get_products().then (data) ->
		$scope.products = data.products

)

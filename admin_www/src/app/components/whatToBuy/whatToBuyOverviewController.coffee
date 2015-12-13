whatToBuy.controller('whatToBuyOverviewController', ($scope, orderProductService, festivalService) ->
	getOrderProducts = orderProductService.getList()
	getOrderProducts.then((response) ->
		$scope.orderProducts = response
	)

	getFestivals = festivalService.getList()
	getFestivals.then((response) ->
		$scope.festivals = response
	)
)

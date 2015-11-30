orders.controller('ordersController', ($scope, userService, authService) ->
	authenticatedUser = authService.getAuthenticatedUser()

	user = userService.one(authenticatedUser.id)
	orders = user.all('orders')
	getOrders = orders.getList()
	getOrders.then((response) ->
		$scope.orders = response
	)
)
orders.controller('orderController', ($scope, $stateParams, userService, authService) ->
	orderId = $stateParams.orderId
	authenticatedUser = authService.getAuthenticatedUser()
	user = userService.one(authenticatedUser.id)
	order = user.one('orders', orderId)
	getOrder = order.get()
	getOrder.then((response) ->
		$scope.order = response
	)
)

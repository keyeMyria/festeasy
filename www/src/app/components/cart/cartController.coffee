cart.controller('cartController', ($scope, $auth, userService) ->
	user_id = $auth.getPayload().sub
	promise = userService.one(user_id).one('cart').get()
	promise.then((response) ->
		$scope.cart = response
	)
	promise.catch((response) ->
		$scope.error = true
	)
)
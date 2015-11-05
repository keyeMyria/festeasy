cart.controller('cartController', ($scope, $auth, userService, cartProductService) ->
	user_id = $auth.getPayload().sub
	cart_promise = userService.one(user_id).one('cart').get()
	cart_promise.then((response) ->
		$scope.cart = response
	)
	cart_promise.catch((response) ->
		$scope.error = true
	)
	cart_product_promise = cartProductService.getList()
	cart_product_promise.then((response) ->
		$scope.cartProducts = response
	)
)
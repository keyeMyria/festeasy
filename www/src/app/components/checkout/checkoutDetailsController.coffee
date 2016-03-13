checkout.controller('checkoutDetailsController', (
	$state, $scope, authService, cartService, userService, festivalService) ->
	$scope.state = $state
	authenticatedUser = authService.getAuthenticatedUser()

	cart = userService.one(authenticatedUser.id).one('cart')

	getCart = cart.get()
	getCart.then((response) ->
		$scope.cart = response
		festival = festivalService.one($scope.cart.festival_id)
		getFestival = festival.get()
		getFestival.then((response) ->
			$scope.festival = response
		)
	)

	getCart.catch((response) ->
		$scope.error = true
	)

	getCartProducts = cart.all('cart-products').getList()
	getCartProducts.then((response) ->
		$scope.cartProducts = response
	)

	$scope.checkout = () ->
		getCart = cart.get()
		getCart.then((response) ->
			checkout = cartService.one(response.id).one('checkout').post()
			checkout.then((response) ->
				order = response
				$state.go('base.checkout.payment', {'order-id': order.id})
			)
		)
)

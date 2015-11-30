checkout.controller('checkoutController', ($state, $scope, authService, cartService, userService) ->
	authenticatedUser = authService.getAuthenticatedUser()
	if not authenticatedUser
		console.log "Please authenticated" 
		return

	cart = userService.one(authenticatedUser.id).one('cart')

	getCart = cart.get()
	getCart.then((response) ->
		$scope.cart = response
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
				$state.go('base.orders')
			)
		)
)

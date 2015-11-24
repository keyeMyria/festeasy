cart.controller('cartController', ($scope, authService, $auth, userService, cartProductService) ->
	authenticatedUser = authService.authenticatedUser()
	if not authenticatedUser
		console.log "Please authenticated" 
		return
	cart = userService.one(authenticatedUser.id).one('cart')
	updateCart = () ->
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
	$scope.remove = (cartProduct) ->
		removeCartProduct = cartProductService.one(cartProduct.id).remove()
		removeCartProduct.then((response) ->
			updateCart()
		)
	$scope.checkout = () ->
		alert 'Would be checking out.'
	updateCart()
)
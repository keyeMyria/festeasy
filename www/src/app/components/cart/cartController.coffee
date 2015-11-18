cart.controller('cartController', ($scope, $auth, userService, cartProductService) ->
	user_id = $auth.getPayload().sub

	cart = userService.one(user_id).one('cart')

	updateCart = () ->
		cart_promise = cart.get()
		cart_promise.then((response) ->
			$scope.cart = response
		)
		cart_promise.catch((response) ->
			$scope.error = true
		)

		cart_product_promise = cart.all('cart-products').getList()
		cart_product_promise.then((response) ->
			$scope.cartProducts = response
		)

	updateCart()

	$scope.remove = (cartProduct) ->
		promise = cartProductService.one(cartProduct.id).remove()
		promise.then((response) ->
			updateCart()
		)
)
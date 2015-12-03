cart.controller('cartController', (
		$scope,
		authService,
		$auth,
		$state,
		userService,
		cartProductService,
		festivalService,
		cartService) ->
	
	authenticatedUser = authService.getAuthenticatedUser()
	if not authenticatedUser
		console.log "Please authenticated" 
		return

	cart = userService.one(authenticatedUser.id).one('cart')

	$scope.updateSelectedFestival = (item, model) ->
		cart.patch({festival_id: item.id})

	updateCart = () ->
		getCart = cart.get()
		getCart.then((response) ->
			$scope.cart = response
			getFestivals = festivalService.getList()
			getFestivals.then((response) ->
				$scope.festivals = response
				if $scope.cart.festival_id
					for festival in $scope.festivals
						if $scope.cart.festival_id == festival.id
							$scope.selectedFestival = festival
			)
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
		$state.go('base.checkout')

	updateCart()
)
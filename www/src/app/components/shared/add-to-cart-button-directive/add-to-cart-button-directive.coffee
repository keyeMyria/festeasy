shared.directive('addToCartButton', () ->
	return {
		restrict: 'E'
		templateUrl: 'add-to-cart-button.partial.html'
		scope: {
			product: '='
		}
		controller: ($scope, authService, userService, notify) ->
			$scope.addToCart = () ->
				authenticatedUser = authService.authenticatedUser()
				if not authenticatedUser
					console.log 'Authenticate to add a product to a cart.'
					return
				user = userService.one(authenticatedUser.id)
				#TODO: Sort out needing to get the cart here.
				cart = user.one('cart')
				getCart = cart.get()
				getCart.then((data) ->
					createCartProduct = cart.post('cart-products', {
						product_id: $scope.product.id,
						cart_id: data.id
					})
					createCartProduct.then((response) ->
						notify 'Added to cart.'
					, (response) ->
						if response.status == 409
							notify 'Item already in cart.'
					)
				)
	}
)
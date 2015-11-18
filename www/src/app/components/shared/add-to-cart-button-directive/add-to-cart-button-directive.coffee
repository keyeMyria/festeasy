shared.directive('addToCartButton', () ->
	return {
		restrict: 'E'
		templateUrl: 'add-to-cart-button.partial.html'
		scope: {
			product: '='
		}
		controller: ($scope, authService, userService) ->
			$scope.addToCart = () ->
				if authService.isAuthenticated()
					user_id = authService.signedinUserId()
					user = userService.one(user_id)
					cart = user.one('cart')
					cart_promise = cart.get()
					cart_promise.then((data) ->
						console.log data.id
						cart.post('cart-products', {
							product_id: $scope.product.id,
							cart_id: data.id
						})
					)
				else
					console.log 'Authenticate to add product to cart.'
	}
)
shared.directive('addToCartButton', () ->
	return {
		restrict: 'E'
		templateUrl: 'add-to-cart-button.partial.html'
		scope: {
			product: '='
		}
		controller: ($scope, authService, userService, ngNotify, $state) ->
			$scope.buttonText = 'Add to cart'
			$scope.isLoading = false
			$scope.addToCart = () ->
				$scope.buttonText = 'Adding to cart'
				$scope.isLoading = true
				authenticatedUser = authService.getAuthenticatedUser()
				if not authenticatedUser
					$state.go('base.signin', {
						redirectReason: 'Auth needed.', 
						message: 'Please sign in to add an item to your cart.'
						returnStateName: $state.current.name
					})
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
						ngNotify.set 'Added to cart.'
					, (response) ->
						if response.status == 409
							ngNotify.set 'Item already in cart.'
					)
					createCartProduct.finally((response) ->
						$scope.buttonText = 'Add to cart'
						$scope.isLoading = false
					)
				)
	}
)

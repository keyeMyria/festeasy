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
				else
					console.log 'Authenticate to add product to cart.'
				alert('Not implemented yet.')
	}
)
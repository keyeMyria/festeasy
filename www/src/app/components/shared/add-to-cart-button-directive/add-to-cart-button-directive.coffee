shared.directive('addToCartButton', () ->
	return {
		restrict: 'E'
		templateUrl: 'add-to-cart-button.partial.html'
		scope: {
			product: '='
		}
		controller: ($scope, authService, userService) ->
			user_id = authService.signedinUserId()
			user = userService.one(user_id)
			$scope.addToCart = () ->
				return
	}
)
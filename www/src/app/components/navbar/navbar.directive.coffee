app.directive('navbar', () ->
	return {
		restrict: 'E'
		transclude: true
		templateUrl: 'navbar.partial.html'
		controller: ($scope, authService) ->
			$scope.isAuthenticated = () ->
				if authService.getAuthenticatedUser()
					return true
				return false
	}
)

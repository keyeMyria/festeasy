app.directive('navbar', () ->
	return {
		restrict: 'E'
		transclude: true
		templateUrl: 'navbar.partial.html'
		controller: ($scope, authService) ->
			$scope.authService = authService
			return
	}
)

app.directive('navbar', () ->
	contorller = ($scope, $stateProvider) ->
		$scope.state = $stateProvider.state

	return {
		restrict: 'E'
		transclude: true
		templateUrl: 'partials/navbar.partial.html'
		contorller: contorller
	}
)

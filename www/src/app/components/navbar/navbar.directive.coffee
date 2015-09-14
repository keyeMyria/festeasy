app.directive('navbar', () ->
	return {
		restrict: 'E'
		transclude: true
		templateUrl: 'partials/navbar.partial.html'
	}
)

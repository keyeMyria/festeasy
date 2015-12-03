shared.directive('loadingIndicator', () ->
	return {
		restrict: 'E'
		templateUrl: 'loadingIndicator.partial.html'
		scope: {
			data: '='
			error: '='
		}
	}
)

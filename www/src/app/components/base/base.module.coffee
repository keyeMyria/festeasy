base = angular.module('base', [
	'ui.router'
])

base.config(($stateProvider) ->
	$stateProvider
		.state('base', {
			abstract: true
			templateUrl: 'partials/base.partial.html'
		})
)

base = angular.module('base', [
	'ui.router'
])

base.config(($stateProvider) ->
	$stateProvider
		.state('base', {
			abstract: true
			templateUrl: 'base.partial.html'
		})
)

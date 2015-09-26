howItWorks = angular.module('howItWorks' , [
	'ui.router'
])

howItWorks.config(($stateProvider) ->
	$stateProvider
		.state('base.how-it-works', {
			url: '/how-it-works'
			templateUrl: 'partials/how-it-works.partial.html'
		})
)
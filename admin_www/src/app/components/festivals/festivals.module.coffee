festivals = angular.module('festivals', [
	'ui.router'
	'services'
])

festivals.config(($stateProvider) ->
	$stateProvider
		.state('base.festivals', {
			url: '/festivals'
			templateUrl: 'festivals.partial.html'
			abstract: true
			auth: true
		})
		.state('base.festivals.overview', {
			url: '/overview'
			templateUrl: 'festivals.overview.partial.html'
			controller: 'festivalsOverviewController'
			auth: true
		})
		.state('base.festivals.festival', {
			url: '/{festivalId:int}'
			templateUrl: 'festival.partial.html'
			controller: 'festivalController'
		})
)

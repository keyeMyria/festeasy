stock = angular.module('stock', [
	'ui.router'
	'shared'
	'services'
	'ngTable'
])

stock.config(($stateProvider) ->
	$stateProvider
		.state('base.stock', {
			url: '/stock'
			templateUrl: 'stock.partial.html'
			abstract: true
			auth: true
		})
		.state('base.stock.overview', {
			url: '/overview'
			templateUrl: 'stock-overview.partial.html'
			controller: 'stockOverviewController'
			auth: true
		})
)

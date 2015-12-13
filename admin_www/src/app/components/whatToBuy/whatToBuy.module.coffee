whatToBuy = angular.module('whatToBuy', [
	'ui.router'
	'services'
	'ui.select'
])

whatToBuy.config(($stateProvider) ->
	$stateProvider
		.state('base.whatToBuy', {
			url: '/what-to-buy'
			templateUrl: 'what-to-buy.partial.html'
			abstract: true
			auth: true
		})
		.state('base.whatToBuy.overview', {
			url: '/overview'
			templateUrl: 'what-to-buy-overview.partial.html'
			controller: 'whatToBuyOverviewController'
			auth: true
		})
)

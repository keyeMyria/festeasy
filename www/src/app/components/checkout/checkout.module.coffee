checkout = angular.module('checkout', [
	'ui.router'
])

checkout.config(($stateProvider) ->
	$stateProvider
		.state('base.checkout', {
			url: '/checkout'
			controller: 'checkoutController'
			templateUrl: 'checkout.partial.html'
			auth: true
		})
)
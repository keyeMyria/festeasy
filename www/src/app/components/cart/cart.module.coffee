cart = angular.module('cart', [
	'ui.router'
	'services'
	'ui.select'
	'shared'
])

cart.config(($stateProvider) ->
	$stateProvider
		.state('base.cart', {
			url: '/cart'
			controller: 'cartController'
			templateUrl: 'cart.partial.html'
			auth: true
		})
)

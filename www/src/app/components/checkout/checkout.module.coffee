checkout = angular.module('checkout', [
	'ui.router'
	'shared'
])

checkout.config(($stateProvider) ->
	$stateProvider
		.state('base.checkout', {
			url: '/checkout'
			controller: 'checkoutController'
			templateUrl: 'checkout.partial.html'
			auth: true
			abstract: true
		})
		.state('base.checkout.details', {
			url: '/details'
			controller: 'checkoutDetailsController'
			templateUrl: 'checkout-details.partial.html'
			auth: true
		})
		.state('base.checkout.confirm-order', {
			url: '/confirm-order'
			controller: 'confirmOrderController'
			templateUrl: 'confirm-order.partial.html'
			auth: true
		})
		.state('base.checkout.payment', {
			url: '/payment'
			controller: 'paymentController'
			templateUrl: 'payment.partial.html'
			auth: true
		})
)

orders = angular.module('orders', [
	'ui.router'
])

orders.config(($stateProvider) ->
	$stateProvider
		.state('base.orders', {
			url: '/account/orders'
			templateUrl: 'orders.partial.html'
			controller: 'ordersController'
		})
		.state('base.order', {
			url: '/account/orders/{orderId:int}'
			templateUrl: 'order.partial.html'
			controller: 'orderController'
		})
)

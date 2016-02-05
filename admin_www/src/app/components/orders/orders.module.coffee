orders = angular.module('orders', [
	'ui.router',
	'services',
	'shared',
])

base.config(($stateProvider) ->
	$stateProvider
		.state('base.orders', {
			templateUrl: 'orders.partial.html'
			controller: 'ordersControlller'
			url: '/orders'
			auth: true
		})
    .state('base.orders.overview', {
      templateUrl: 'orders-overview.partial.html'
      controller: 'ordersOverviewController'
      url: '/overview'
      auth: true
    })
		.state('base.orders.order', {
			templateUrl: 'order.partial.html'
			controller: 'orderController'
			url: '/{orderId:int}'
			auth: true
		})
)

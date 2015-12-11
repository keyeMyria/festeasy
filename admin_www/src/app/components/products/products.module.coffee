products = angular.module('products', [
	'ui.router',
])

base.config(($stateProvider) ->
	$stateProvider
		.state('base.products', {
			templateUrl: 'products.partial.html'
			controller: 'productsController'
			url: '/products'
			auth: true
		})
)

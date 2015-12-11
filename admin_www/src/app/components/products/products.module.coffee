products = angular.module('products', [
	'ui.router',
	'shared',
	'services',
])

base.config(($stateProvider) ->
	$stateProvider
		.state('base.products', {
			templateUrl: 'products.partial.html'
			controller: 'productsController'
			url: '/products'
			auth: true
			abstract: true
		})
		.state('base.products.overview', {
			templateUrl: 'products.overview.partial.html'
			url: '/overview'
			auth: true
		})
		.state('base.products.create', {
			templateUrl: 'products.create.partial.html'
			url: '/create'
			auth: true
		})
		.state('base.products.product', {
			templateUrl: 'product.partial.html'
			url: '/{productId:int}'
			controller: 'productController'
			auth: true
		})
)

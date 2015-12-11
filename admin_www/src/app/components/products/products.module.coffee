products = angular.module('products', [
	'ui.router',
	'shared',
	'services',
])

base.config(($stateProvider) ->
	$stateProvider
		.state('base.products', {
			templateUrl: 'products.partial.html'
			url: '/products'
			auth: true
			abstract: true
		})
		.state('base.products.overview', {
			templateUrl: 'products.overview.partial.html'
			controller: 'productsOverviewController'
			url: '/overview'
			auth: true
		})
		.state('base.products.create', {
			templateUrl: 'products.create.partial.html'
			controller: 'createProductController'
			url: '/create'
			auth: true
		})
		.state('base.products.product', {
			templateUrl: 'product.partial.html'
			controller: 'productController'
			url: '/{productId:int}'
			auth: true
		})
)

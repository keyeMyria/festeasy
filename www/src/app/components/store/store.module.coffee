store = angular.module('store', [
	'ui.router'
	'services'
	'shared'
])

store.config(($stateProvider) ->
    $stateProvider
        .state('base.store', {
            url: '/store?category'
            templateUrl: 'store.partial.html'
            controller: 'storeController'
            abstract: true
        })
        .state('base.store.products', {
            url: '/products?search'
            templateUrl: 'products.partial.html'
            controller: 'productsController'
        })
        .state('base.store.product', {
        	url: '/products/{productId:int}'
        	templateUrl: 'product.partial.html'
        	controller: 'productController'
       	})
)

store = angular.module('store', [
	'ui.router'
	'services'
	'shared'
])

store.config(($stateProvider) ->
    $stateProvider
        .state('base.store', {
            url: '/store?category&search'
            templateUrl: 'store.partial.html'
            controller: 'storeController'
        })
        .state('base.product', {
        	url: '/store/products/{productId:int}'
        	templateUrl: 'product.partial.html'
        	controller: 'productController'
       	})
)
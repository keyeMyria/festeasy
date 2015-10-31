store = angular.module('store', [
	'ui.router'
	'services'
])

store.config(($stateProvider) ->
    $stateProvider
        .state('base.store', {
            url: '/store'
            templateUrl: 'store.partial.html'
            controller: 'storeController'
        })
)

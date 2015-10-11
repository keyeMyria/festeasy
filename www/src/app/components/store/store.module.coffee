store = angular.module('store', [
	'ui.router'
	'services'
])

store.config(($stateProvider) ->
    $stateProvider
        .state('base.store', {
            url: '/store'
            templateUrl: 'partials/store.partial.html'
            controller: 'storeController'
        })
)

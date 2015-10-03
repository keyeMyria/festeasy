store = angular.module('store', [
	'ui.router'
])

store.config(($stateProvider) ->
    $stateProvider
        .state('base.store', {
            url: '/store'
            templateUrl: 'partials/store.partial.html'
        })
)

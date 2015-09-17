landing = angular.module('landing', [
	'ui.router',
])

landing.config(($stateProvider) ->
    $stateProvider
        .state('landing', {
            url: '/'
            templateUrl: 'partials/landing.partial.html'
        })
)

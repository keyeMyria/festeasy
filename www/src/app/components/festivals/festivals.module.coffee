festivals = angular.module('festivals', [
	'ui.router',
])

festivals.config(($stateProvider) ->
    $stateProvider
        .state('base.festivals', {
            url: '/festivals'
            templateUrl: 'partials/festivals.partial.html'
            controller: 'festivalsController'
        })
)

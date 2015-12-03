festivals = angular.module('festivals', [
	'ui.router',
	'shared'
])

festivals.config(($stateProvider) ->
    $stateProvider
        .state('base.festivals', {
            url: '/festivals'
            templateUrl: 'festivals.partial.html'
            controller: 'festivalsController'
        })
)

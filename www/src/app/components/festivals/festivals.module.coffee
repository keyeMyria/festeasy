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
        .state('base.festivals.festival', {
        	url: '/{festivalId:int}'
        	templateUrl: 'festival.partial.html'
        	controller: 'festivalController'
        })
)

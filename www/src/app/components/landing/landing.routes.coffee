landing.config(($stateProvider, $urlRouterProvider) ->
    $stateProvider
        .state('landing', {
            url: '/'
            templateUrl: 'partials/landing.partial.html'
        })
)

landing.config(($stateProvider, $urlRouterProvider) ->
    $stateProvider
        .state('landing', {
            url: '/'
            templateUrl: 'app/components/landing/landingView.html'
        })
)

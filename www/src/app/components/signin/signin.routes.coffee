signin.config(($stateProvider, $urlRouterProvider) ->
    $stateProvider
        .state('siginin', {
            url: '/signin'
            templateUrl: 'app/components/signin/signin.partial.html'
        })
)

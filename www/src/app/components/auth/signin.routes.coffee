signin.config(($stateProvider, $urlRouterProvider) ->
    $stateProvider
        .state('signin', {
            url: '/signin'
            templateUrl: 'app/components/auth/signin.partial.html'
        })
)

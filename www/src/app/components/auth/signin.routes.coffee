signin.config(($stateProvider, $urlRouterProvider) ->
    $stateProvider
        .state('signin', {
            url: '/signin'
            templateUrl: 'partials/signin.partial.html'
        })
)

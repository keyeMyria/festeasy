app = angular.module('app', [
    'base'
    'landing',
    'auth',
    'account',
])

app.config(($locationProvider) ->
    $locationProvider.html5Mode({
        enabled: true,
    })
)

app.run(($rootScope, $auth, $state) ->
    $rootScope.$on('$stateChangeStart',
        (event, toState, toParams, fromState, fromParams) ->
            if toState.auth and not $auth.isAuthenticated()
                event.preventDefault()
                $state.go('base.signin')
))

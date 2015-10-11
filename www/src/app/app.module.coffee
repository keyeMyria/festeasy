app = angular.module('app', [
    'base'
    'landing'
    'auth'
    'account'
    'festivals'
    'store'
    'howItWorks'
    'cart'
])

app.config(($locationProvider) ->
    $locationProvider.html5Mode({
        enabled: true,
    })
)

app.config(($stateProvider, $urlRouterProvider) ->
    $urlRouterProvider
        .otherwise('/')
)

app.run(($rootScope, authService, $state) ->
    $rootScope.$on('$stateChangeStart',
        (event, toState, toParams, fromState, fromParams) ->
            if toState.auth and not authService.isAuthenticated()
                event.preventDefault()
                $state.go('base.signin', {redirectReason: 'Auth needed.'})
    )
    $rootScope.$on('$stateNotFound',
        (event, unfoundState, fromState, fromParams) ->
            console.log 'State not found.'
    )
)

app = angular.module('app', [
    'ngNotify'
    'base'
    'landing'
    'auth'
    'account'
    'festivals'
    'store'
    'howItWorks'
    'cart'
    'orders'
    'checkout'
    'services'
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
            if toState.auth and not authService.getAuthenticatedUser()
                event.preventDefault()
                $state.go('base.signin', {redirectReason: 'Auth needed.', message: 'Please sign in to see that page.'})
    )
    $rootScope.$on('$stateNotFound',
        (event, unfoundState, fromState, fromParams) ->
            console.log 'State not found.'
    )
)

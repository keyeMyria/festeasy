app = angular.module('app', [
    'ui.router', 
    'restangular',
    'LocalStorageModule',
    'cgNotify',
])

app.config(($stateProvider, $urlRouterProvider) ->
    $urlRouterProvider
        .otherwise('/')
        
    $stateProvider
        .state('base', {
            abstract: true
            url: '/'
            templateUrl: 'partials/base.html'
            controller: 'BaseController'
            auth_required: true
        })
        .state('base.landing', {
            url: ''
            templateUrl: 'partials/base.landing.html'
            auth_required: true
        })
        .state('base.signin', {
            url: 'signin'
            templateUrl: 'partials/base.signin.html'
            controller: 'SigninController'
            auth_required: false
        })
        .state('base.products', {
            url: 'products'
            templateUrl: 'partials/base.products.html'
            controller: 'ProductsController'
            auth_required: true
        })
)

app.config((RestangularProvider, API_END_POINT) ->
    RestangularProvider.setBaseUrl(API_END_POINT)
)

app.config((localStorageServiceProvider) ->
    localStorageServiceProvider
        .setPrefix('festeasy')
        .setStorageType('sessionStorage')
        .setNotify(true, true)
)

app.run(($rootScope, $state, $stateParams) ->
    $rootScope.$state = $state
    $rootScope.$stateParams = $stateParams
)

app.run((notify) ->
    notify.config(
        duration: 3000, 
        position: 'center', 
        templateUrl: 'templates/notification.html'
    )
)

app.run((Restangular, $state, userService) ->
    Restangular.setErrorInterceptor((error) ->
        if error.status == 401 and $state.current.name != 'base.signin'
            userService.signout()
    )
)

app.run((userService) ->
    userService.load_session_from_cookie()
    if userService.is_signed_in()
        userService.get()
)

auth = angular.module('auth', [
	'ui.router',
	'satellizer',
	'conf',
])

auth.config(($authProvider, API_END_POINT) ->
	$authProvider.httpInterceptor = true
	$authProvider.withCredentials = true
	$authProvider.tokenRoot = null
	$authProvider.cordova = false
	$authProvider.baseUrl = API_END_POINT
	$authProvider.loginUrl = '/signin'
	$authProvider.signupUrl = '/signup'
	$authProvider.unlinkUrl = '/auth/unlink/'
	$authProvider.tokenName = 'token'
	$authProvider.tokenPrefix = 'satellizer'
	$authProvider.authHeader = 'Authorization'
	$authProvider.authToken = 'Bearer'
	$authProvider.storageType = 'localStorage'
)

auth.config(($stateProvider) ->
    $stateProvider
        .state('base.signin', {
            url: '/signin'
            templateUrl: 'partials/signin.partial.html'
            controller: 'signinController'
        })
        .state('base.signup', {
            url: '/signup'
            templateUrl: 'partials/signup.partial.html'
            controller: 'signupController'
        })
)

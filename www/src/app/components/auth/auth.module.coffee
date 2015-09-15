auth = angular.module('auth', [
	'ui.router',
	'satellizer',
])

auth.config(($authProvider) ->
	$authProvider.httpInterceptor = true;
	$authProvider.withCredentials = true;
	$authProvider.tokenRoot = null;
	$authProvider.cordova = false;
	$authProvider.baseUrl = 'http://localhost:5000/api/v1/';
	$authProvider.loginUrl = '/signin';
	$authProvider.signupUrl = '/signup';
	$authProvider.unlinkUrl = '/auth/unlink/';
	$authProvider.tokenName = 'token';
	$authProvider.tokenPrefix = 'satellizer';
	$authProvider.authHeader = 'Authorization';
	$authProvider.authToken = 'Bearer';
	$authProvider.storageType = 'localStorage';
)

auth.config(($stateProvider, $urlRouterProvider) ->
    $stateProvider
        .state('signin', {
            url: '/signin'
            templateUrl: 'partials/signin.partial.html'
            controller: 'signinController'
        })
)

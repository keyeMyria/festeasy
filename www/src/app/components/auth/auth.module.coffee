auth = angular.module('auth', [
	'ui.router',
	'satellizer',
	'conf',
	'services',
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
	$authProvider.facebook({
	  name: 'facebook',
	  url: '/auth/facebook',
	  authorizationEndpoint: 'https://www.facebook.com/v2.5/dialog/oauth',
	  redirectUri: window.location.origin + '/',
	  requiredUrlParams: ['display', 'scope'],
	  scope: ['email'],
	  scopeDelimiter: ',',
	  display: 'popup',
	  type: '2.0',
	  popupOptions: { width: 580, height: 400 }
	});
)

auth.config(($stateProvider) ->
    $stateProvider
        .state('base.signin', {
            url: '/signin?returnStateName'
            templateUrl: 'signin.partial.html'
            controller: 'signinController'
            params: {
            	redirectReason: null
            	message: null
            }
        })
        .state('base.signup', {
            url: '/signup?returnStateName'
            templateUrl: 'signup.partial.html'
            controller: 'signupController'
        })
        .state('base.forgot-password', {
        	url: '/forgot-password'
        	templateUrl: 'forgot-password.partial.html'
        	controller: 'forgotPasswordController'
        })
        .state('base.reset-password', {
            url: '/reset-password?token'
            templateUrl: 'reset-password.partial.html'
            controller: 'resetPasswordController'
        })
)

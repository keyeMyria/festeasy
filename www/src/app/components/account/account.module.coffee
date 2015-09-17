account = angular.module('account', [
	'ui.router'
	'services'
])

account.config(($stateProvider) ->
	$stateProvider
        .state('account', {
            url: '/account'
            templateUrl: 'partials/account.partial.html'
            controller: 'accountController'
            resolve: 
            	user: ($auth, userService) ->
            		user_id = $auth.getPayload().sub
            		return userService.one(user_id).get()
        })
)

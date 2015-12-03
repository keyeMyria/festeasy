account = angular.module('account', [
	'ui.router'
	'services'
	'shared'
])

account.config(($stateProvider) ->
	$stateProvider
        .state('base.account', {
            url: '/account'
            templateUrl: 'account.partial.html'
            controller: 'accountController'
            auth: true
        })
)

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
        })
)

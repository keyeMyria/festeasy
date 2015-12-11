users = angular.module('users', [
	'ui.router',
	'services',
	'shared',
])

base.config(($stateProvider) ->
	$stateProvider
		.state('base.users', {
			templateUrl: 'users.partial.html'
			controller: 'usersController'
			url: '/users'
			auth: true
		})
)

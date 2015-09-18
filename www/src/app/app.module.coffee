app = angular.module('app', [
	'base'
	'landing',
	'auth',
	'account',
])

app.config(($locationProvider) ->
    $locationProvider.html5Mode({
        enabled: true,
    })
)

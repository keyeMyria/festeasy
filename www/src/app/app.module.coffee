app = angular.module('app', [
	'landing',
	'auth',
	'ui.router',
])

app.config(($locationProvider) ->
    $locationProvider.html5Mode({
        enabled: true,
    })
)

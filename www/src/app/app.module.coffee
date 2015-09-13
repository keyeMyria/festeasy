app = angular.module('app', [
	'landing',
	'signin',
	'ui.router',
])

app.config(($locationProvider) ->
    $locationProvider.html5Mode({
        enabled: true,
    })
)

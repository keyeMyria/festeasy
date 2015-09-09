app = angular.module('app', [
	'landing',
	'ui.router',
])

app.config(($locationProvider) ->
    $locationProvider.html5Mode({
        enabled: true,
    })
)

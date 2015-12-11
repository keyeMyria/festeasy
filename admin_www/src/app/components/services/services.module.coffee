services = angular.module('services', [
	'conf',
	'restangular'
])

services.config((RestangularProvider, API_END_POINT) ->
	RestangularProvider.setBaseUrl(API_END_POINT)
)

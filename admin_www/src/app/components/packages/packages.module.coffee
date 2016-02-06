packages = angular.module('packages', [
	'ui.router',
	'shared',
	'services',
])

base.config(($stateProvider) ->
	$stateProvider
		.state('base.packages', {
			templateUrl: 'packages.partial.html'
			url: '/packages'
			auth: true
			abstract: true
		})
		.state('base.packages.overview', {
			templateUrl: 'packages.overview.partial.html'
			controller: 'packagesOverviewController'
			url: '/overview'
			auth: true
    })
    .state('base.packages.package', {
      templateUrl: 'package.partial.html'
      controller: 'packageController'
      url: '/{packageId:int}'
      auth: true
    })
)

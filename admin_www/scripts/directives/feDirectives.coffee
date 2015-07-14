app.directive('myGreetingNavbarText', [() ->
	return {
		restrict: 'AE'
		templateUrl: 'templates/my-greeting-navbar-text.html'
		scope: {
			firstName: '='
		}
	}
])


app.directive('mySignInNavButton', ['userService', '$state', (userService, $state) ->

	return {
		restrict: 'AE'
		templateUrl: 'templates/my-sign-in-nav-button.html'
	}
])

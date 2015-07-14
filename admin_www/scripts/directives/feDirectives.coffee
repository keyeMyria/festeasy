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

app.directive('myPrice', [() ->
	return {
		restrict: 'A',
		templateUrl: 'templates/my-price.html',
		scope: {
			amount: '='
		}
	}
])

app.directive('myProduct', [() ->
	return {
		restrict: 'E',
		templateUrl: 'templates/my-product.html',
		scope: {
			product: '='
		}
	}
])
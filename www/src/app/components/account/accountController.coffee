account.controller('accountController', ($scope, $auth, userService, authService) ->
	authenticatedUser = authService.getAuthenticatedUser()
	promise = userService.one(authenticatedUser.id).get()
	promise.then((response) ->
		$scope.user = response
	)
	promise.catch((response) ->
		$scope.error = true
	)
)

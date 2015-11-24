account.controller('accountController', ($scope, $auth, userService, authService) ->
	user = authService.authenticatedUser()
	promise = userService.one(user.id).get()
	promise.then((response) ->
		$scope.user = response
	)
	promise.catch((response) ->
		$scope.error = true
	)
)

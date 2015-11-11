account.controller('accountController', ($scope, $auth, userService, authService) ->
	user_id = authService.signedinUserId()
	promise = userService.one(user_id).get()
	promise.then((response) ->
		$scope.user = response
	)
	promise.catch((response) ->
		$scope.error = true
	)
)

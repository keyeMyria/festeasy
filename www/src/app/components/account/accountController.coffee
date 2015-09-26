account.controller('accountController', ($scope, $auth, userService) ->
	user_id = $auth.getPayload().sub
	promise = userService.one(user_id).get()
	promise.then((response) ->
		$scope.user = response
	)
	promise.catch((response) ->
		$scope.error = true
	)
)

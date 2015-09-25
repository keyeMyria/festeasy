account.controller('accountController', ($scope, $auth, userService) ->
	$scope.is_loading = true
	user_id = $auth.getPayload().sub
	promise = userService.one(user_id).get()
	promise.then((response) ->
		$scope.is_loading = false
		$scope.user = response
	)
)

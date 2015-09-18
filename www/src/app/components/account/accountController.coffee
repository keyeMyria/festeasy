account.controller('accountController', ($scope, $auth, userService, $state) ->
	if not $auth.isAuthenticated()
		$state.go('base.signin')
		return

	$scope.is_loading = true
	user_id = $auth.getPayload().sub
	promise = userService.one(user_id).get()
	promise.then((response) ->
		console.log response
		$scope.is_loading = false
		$scope.user = response
	)
)

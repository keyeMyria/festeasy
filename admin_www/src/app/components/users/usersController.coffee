users.controller('usersController', ($scope, userService) ->
	$scope.error = false
	getUsers = userService.getList()
	getUsers.then((repsonse) ->
		$scope.users = repsonse
	)
	getUsers.catch((repsonse) ->
		$scope.error = true
	)
)

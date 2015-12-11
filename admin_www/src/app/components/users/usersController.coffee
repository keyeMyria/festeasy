users.controller('usersController', ($scope, userService) ->
	getUsers = userService.getList()
	getUsers.then((repsonse) ->
		$scope.users = repsonse
	)
)
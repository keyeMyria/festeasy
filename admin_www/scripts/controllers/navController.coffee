app.controller('NavController', ($scope, userService) ->
	$scope.userService = userService

	$scope.$watch('userService.get_user()', (newValue, oldValue) ->
		$scope.user = newValue
	)

	$scope.has_signed_up = () ->
		if userService.is_signed_in() and not userService.is_guest()
			return true
		return false
)

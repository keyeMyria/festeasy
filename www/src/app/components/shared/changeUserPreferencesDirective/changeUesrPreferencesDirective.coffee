shared.directive('changeUserPreferences', () ->
	controller = ($scope, userService, ngNotify) ->
		$scope.changeUserPreferences = () ->
			user = userService.one($scope.user.id)
			patchUser = user.patch($scope.user)
			patchUser.then((response) ->
				$scope.user = response
				ngNotify.set('Saved changes')
			)
	return {
		restrict: 'E'
		templateUrl: 'change-user-preferences.partial.html'
		scope: {
			user: '='
		}
		controller: controller
	}
)

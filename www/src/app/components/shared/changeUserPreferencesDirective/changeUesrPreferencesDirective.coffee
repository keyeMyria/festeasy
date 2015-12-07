shared.directive('changeUserPreferences', () ->
	controller = ($scope, userService, ngNotify) ->
		console.log $scope.data.user
		$scope.tmp = {
			first_name: $scope.data.user.first_name
			last_name: $scope.data.user.last_name
		}
		$scope.changeUserPreferences = () ->
			user = userService.one($scope.data.user.id)
			patchUser = user.patch($scope.tmp)
			patchUser.then((response) ->
				$scope.data.user = response
				ngNotify.set('Saved changes')
			)
			patchUser.catch((response) ->
				ngNotify.set('Failed to save changes.', 'error')
			)
	return {
		restrict: 'E'
		templateUrl: 'change-user-preferences.partial.html'
		controller: controller
	}
)

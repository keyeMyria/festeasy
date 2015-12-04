shared.directive('changePassword', () ->
	controller = ($scope, userService, authService, ngNotify) ->
		authenticatedUser = authService.getAuthenticatedUser()
		if not authenticatedUser
			console.log 'Need to be authenticated to show change password form'
			return
		$scope.data = {
			currentPassword: null
			newPassword: null
		}
		$scope.submitted = false
		$scope.changePassword = () ->
			$scope.submitted = true
			serializedData = {
				current_password: $scope.data.currentPassword
				new_password: $scope.data.newPassword
			}
			user = userService.one(authenticatedUser.id)
			changePassword = user.all('change-password').post(serializedData)
			changePassword.then((response) ->
				$scope.data = {
					currentPassword: null
					newPassword: null
				}
				ngNotify.set('Sucessfully changed password.')

			)
			changePassword.catch((response) ->
				ngNotify.set('Failed to change password. Please try again.', 'error')
			)
	return {
		restrict: 'E'
		templateUrl: 'change-password.partial.html'
		controller: controller
	}
)
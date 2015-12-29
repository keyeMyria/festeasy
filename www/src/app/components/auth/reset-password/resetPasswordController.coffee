auth.controller('resetPasswordController', ($scope, $stateParams, authService,
		resetPasswordService, ngNotify) ->
	$scope.password1 = null
	$scope.password2 = null
	$scope.resetPassword = () ->
		$scope.message = null
		if $scope.password1 != $scope.password2
			ngNotify.set('Passwords do not match.', 'error')
			return
		params = {
			token: $stateParams.token
			password: $scope.password1
		}
		post = resetPasswordService.post(params)
		post.then((response) ->
			ngNotify.set('Successfully reset password.')
			$scope.message = 'You may now sign in with your new password.'
		)
		post.catch((response) ->
			ngNotify.set('Failed to reset password.', 'error')
		)
)

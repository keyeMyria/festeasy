auth.controller('signupController', ($scope, authService, $state) ->
	$scope.user = {
		email_address: null
		password: null
		first_name: null
	}
	$scope.signup = () ->
		$scope.errors = {
			connection_error: null
			unknown_error: null
		}
		$scope.is_loading = true
		promise = authService.signup($scope.user)
		promise.then((response) ->
			console.log 'success'
			$state.go('base.account')
		, (response) ->
			console.log 'fail'
			status_code = response.status
			if status_code == 0
				$scope.errors.connection_error = true
			else
				$scope.errors.unknown_error = true
		)
		promise.finally((response) ->
			$scope.is_loading = false
		)
)

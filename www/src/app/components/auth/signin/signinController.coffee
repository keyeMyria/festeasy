auth.controller('signinController', ($scope, authService, $state, $stateParams) ->
	$scope.redirectReason = $stateParams.redirectReason
	$scope.redirectMessage = $stateParams.message
	returnStateName = $stateParams.returnStateName
	$scope.user = {
		email_address: null
		password: null
	}
	$scope.signin = () ->
		$scope.errors = {
			connection_error: null
			auth_error: null
			unknown_error: null
		}
		$scope.is_loading = true
		$scope.redirectReason = null
		promise = authService.signin($scope.user)
		promise.then((response) ->
			console.log 'success'
			if returnStateName
				console.log returnStateName
				$state.go(returnStateName)
			else
				$state.go('base.store.products')
		, (response) ->
			console.log 'fail'
			status_code = response.status
			if status_code == 0
				$scope.errors.connection_error = true
			else if status_code == 401
				$scope.errors.auth_error = true
			else
				$scope.errors.unknown_error = true
		)
		promise.finally((response) ->
			$scope.is_loading = false
		)
)

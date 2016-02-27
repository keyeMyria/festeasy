auth.controller('signinController', ($auth, $scope, authService, $state, $stateParams) ->
	$scope.redirectReason = $stateParams.redirectReason
	$scope.redirectMessage = $stateParams.message
	returnStateName = $stateParams.returnStateName
	$scope.user = {
		email_address: null
		password: null
	}
	$scope.isLoading = false

	$scope.authenticate = (provider) ->
		$scope.isLoading = true
		p = $auth.authenticate(provider)
		p.then((response) ->
			$state.go('base.store.products')
		)
		p.finally((response) ->
			$scope.isLoading = false
		)

	$scope.signin = () ->
		$scope.errors = {
			connection_error: null
			auth_error: null
			unknown_error: null
		}
		$scope.isLoading = true
		$scope.redirectReason = null
		promise = authService.signin($scope.user)
		promise.then((response) ->
			if returnStateName
				window.history.back()
			else
				$state.go('base.store.products')
		, (response) ->
			status_code = response.status
			if status_code == 0
				$scope.errors.connection_error = true
			else if status_code == 401
				$scope.errors.auth_error = true
			else
				$scope.errors.unknown_error = true
		)
		promise.finally((response) ->
			$scope.isLoading = false
		)
)

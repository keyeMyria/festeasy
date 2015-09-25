auth.controller('signinController', ($scope, authService, $state, $stateParams) ->
	$scope.is_loading = false
	$scope.redirectReason = $stateParams.redirectReason
	$scope.user = {
		email_address: null
		password: null
	}
	$scope.errors = {
		auth_error: null
	}
	$scope.signin = () ->
		$scope.is_loading = true
		$scope.redirectReason = null
		$scope.errors.auth_error = false
		promise = authService.signin($scope.user)
		promise.then((response) ->
			console.log 'success'
			$state.go('base.account')
		, (response) ->
			console.log 'fail'
			$scope.errors.auth_error = true
		)
		promise.finally((response) ->
			$scope.is_loading = false
		)
)

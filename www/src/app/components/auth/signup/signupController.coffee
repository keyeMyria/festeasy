auth.controller('signupController', ($scope, authService, $state, $auth) ->
	$scope.user = {
		email_address: null
		password: null
		first_name: null
	}
	$scope.authenticate = (provider) ->
		$scope.isLoading = true
		p = $auth.authenticate(provider)
		p.then((response) ->
			$state.go('base.store.products')
		)
		p.finally((response) ->
			$scope.isLoading = false
		)
	$scope.signup = () ->
		$scope.errors = {
			connection_error: null
			duplicate_error: null
			unknown_error: null
		}
		$scope.isLoading = true
		promise = authService.signup($scope.user)
		promise.then((response) ->
			console.log 'success'
			$state.go('base.account')
		, (response) ->
			console.log 'fail'
			status_code = response.status
			if status_code == 0
				$scope.errors.connection_error = true
			else if status_code == 409
				$scope.errors.duplicate_error = true
			else
				$scope.errors.unknown_error = true
		)
		promise.finally((response) ->
			$scope.isLoading = false
		)
)

auth.controller('signupController', ($scope, authService, $state) ->
	$scope.is_loading = false
	$scope.user = {
		email_address: null
		password: null
		first_name: null
	}
	$scope.errors = {
		auth_error: null
	}
	$scope.signup = () ->
		$scope.is_loading = true
		$scope.errors.auth_error = false
		promise = authService.signup($scope.user)
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

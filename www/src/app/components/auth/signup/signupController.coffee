auth.controller('signupController', ($scope, authService, $state) ->
	$scope.user = {
		email_address: null
		password: null
		first_name: null
	}
	$scope.errors = {
		auth_error: null
	}
	$scope.signup = () ->
		$scope.errors.auth_error = false
		promise = authService.signup($scope.user)
		promise.then((response) ->
			console.log 'success'
			console.log response
			$state.go('base.account')
		, (response) ->
			console.log 'fail'
			$scope.errors.auth_error = true
			console.log response
		, (response) ->
			console.log 'notify'
			console.log response
		)
)

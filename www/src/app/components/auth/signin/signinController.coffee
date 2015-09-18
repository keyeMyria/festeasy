auth.controller('signinController', ($scope, authService, $state) ->
	$scope.user = {
		email_address: null
		password: null
	}
	$scope.errors = {
		auth_error: null
	}
	$scope.signin = () ->
		$scope.errors.auth_error = false
		promise = authService.signin($scope.user)
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

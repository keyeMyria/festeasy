auth.controller('signinController', ($scope, authService) ->
	$scope.user = {
		email_address: null
		password: null
	}
	$scope.signin = () ->
		authService.signin($scope.user)
)

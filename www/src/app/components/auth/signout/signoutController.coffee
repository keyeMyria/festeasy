auth.controller('signoutController', ($scope, $auth, $state) ->
	$scope.signout = () ->
		$auth.logout().then(() ->
			$state.go('base.landing')
		)
)

festivals.controller('festivalsController', ($scope, $state, festivalService, authService, userService) ->
	getFestivals = festivalService.getList()
	getFestivals.then((response) ->
		$scope.festivals = response
	)
	getFestivals.catch((response) ->
		$scope.error = true
	)
	
	$scope.selectFestival = (festival) ->
		authenticatedUser = authService.authenticatedUser()
		if authenticatedUser
			cart = userService.one(authenticatedUser.id).one('cart')
			console.log 'signed in'
			patchCart = cart.patch({festival_id: festival.id})
			patchCart.then((response) ->
				$state.go('base.store')
			)
		else
			$state.go('base.signin', {redirectReason: 'Auth needed.', message: 'Please sign in to select a festival.'})
)

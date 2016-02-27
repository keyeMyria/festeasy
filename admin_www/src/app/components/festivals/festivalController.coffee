festivals.controller('festivalController', ($scope, festivalService, ngNotify, $stateParams) ->
	$scope.error = false
	festivalId = $stateParams.festivalId
	festival = festivalService.one(festivalId)
	getFestival = festival.get()
	getFestival.then((repsonse) ->
		$scope.festival = repsonse
	)
	getFestival.catch((repsonse) ->
		$scope.error = true
	)

	$scope.updateFestival = (festival) ->
		patchFestival = festival.patch(festival)
		patchFestival.then((repsonse) ->
			ngNotify.set('Successfully updated product.')
		)
		patchFestival.catch((repsonse) ->
			ngNotify.set('Failed to update product.', 'error')
		)
)

festivals.controller('festivalController', ($scope, festivalService, $stateParams) ->
	festivalId = $stateParams.festivalId
	festival = festivalService.one(festivalId)
	getFestival = festival.get()
	getFestival.then((response) ->
		$scope.festival = response
	)
)
festivals.controller('festivalsController', ($scope, festivalService) ->
	getFestivals = festivalService.getList()
	getFestivals.then((response) ->
		$scope.festivals = response
	)
	getFestivals.catch((response) ->
		$scope.error = true
	)
)

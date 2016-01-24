festivals.controller('festivalsOverviewController', ($scope, festivalService) ->
	$scope.error = false
	getFestivals = festivalService.getList()
	getFestivals.then((response) ->
		$scope.festivals = response
	)
	getFestivals.catch((response) ->
		$scope.error = true
	)
)

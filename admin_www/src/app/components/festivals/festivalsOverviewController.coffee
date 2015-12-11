festivals.controller('festivalsOverviewController', ($scope, festivalService) ->
	getFestivals = festivalService.getList()
	getFestivals.then((response) ->
		$scope.festivals = response
	)
)

festivals.controller('festivalsController', ($scope, festivalService) ->
	$scope.isLoading = true
	promise = festivalService.getList()
	promise.then((response) ->
		$scope.festivals = response
	)
	promise.finally((response) ->
		$scope.isLoading = false
	)
)

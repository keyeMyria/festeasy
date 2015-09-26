festivals.controller('festivalsController', ($scope, festivalService) ->
	promise = festivalService.getList()
	promise.then((response) ->
		$scope.festivals = response
	)
	promise.catch((response) ->
		$scope.error = true
	)
)

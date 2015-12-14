whatToBuy.controller('whatToBuyOverviewController', ($scope, $state, orderProductService, festivalService, $stateParams) ->
	params = {}
	if $stateParams['festival-id']
		params['festival-id'] = $stateParams['festival-id']

	fetchOrderProducts = (params) ->
		getOrderProducts = orderProductService.getList(params)
		getOrderProducts.then((response) ->
			$scope.orderProducts = response
		)

	setSelectedFestival = (params) ->
		if params['festival-id']
			for festival in $scope.festivals
				if parseInt(festival.id) == parseInt(params['festival-id'])
					$scope.selectedFestival = festival

	fetchFestivals = () ->
		getFestivals = festivalService.getList()
		getFestivals.then((response) ->
			$scope.festivals = response
			setSelectedFestival(params)
		)

	fetchOrderProducts(params)
	fetchFestivals()

	$scope.updateSelectedFestival = (festival, something) ->
		params['festival-id'] = festival.id
		$state.go('base.whatToBuy.overview', params, {reload: true})
)

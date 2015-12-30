whatToBuy.controller('whatToBuyOverviewController', (
		$scope, $state, orderProductService, festivalService, $stateParams, productStockService) ->
	params = {}
	if $stateParams['festival-id']
		params['festival-id'] = $stateParams['festival-id']

	fetchProductStocks = () ->
		getProductStocks = productStockService.getList()
		getProductStocks.then((response) ->
			$scope.productStocks = response
		)

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

	$scope.updateSelectedFestival = (festival, something) ->
		params['festival-id'] = festival.id
		$state.go('base.whatToBuy.overview', params, {reload: true})

	$scope.countProductStocks = (product, productStocks) ->
		count = 0
		for produtStock in productStocks
			if product.id == produtStock.product.id
				count += 1
		return count

	fetchOrderProducts(params)
	fetchProductStocks()
	fetchFestivals()
)

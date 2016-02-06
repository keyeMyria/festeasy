whatToBuy.controller('whatToBuyOverviewController', (
		$scope, $state, orderProductService, festivalService, $stateParams, stockUnitService) ->
	params = {}
	$scope.error = false
	if $stateParams['festival-id']
		params['festival-id'] = $stateParams['festival-id']

	fetchStockUnits = () ->
		getStockUnits = stockUnitService.getList()
		getStockUnits.then((response) ->
			$scope.stockUnits = response
		)
		getStockUnits.catch((response) ->
			$scope.error = true
		)

	fetchOrderProducts = (params) ->
		getOrderProducts = orderProductService.getList(params)
		getOrderProducts.then((response) ->
			$scope.orderProducts = response
		)
		getOrderProducts.catch((response) ->
			$scope.error = true
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
		getFestivals.catch((response) ->
			$scope.error = true
		)

	$scope.updateSelectedFestival = (festival, something) ->
		params['festival-id'] = festival.id
		$state.go('base.whatToBuy.overview', params, {reload: true})

	# TODO: Implement proper solution for this.
	# This is being called for each row in a table in the view, help!
	$scope.sumOrderProductQuantities = (orderProducts) ->
		result = {}
		for op in orderProducts
			if op.product.id in result
				result[op.product.id] += op.quantity
			else
				result[op.product.id] = op.quantity
		return result

	$scope.countStockUnits = (product, stockUnits) ->
		count = 0
		for stockUnit in stockUnits
			if product.id == stockUnit.product.id
				count += 1
		return count

	fetchOrderProducts(params)
	fetchStockUnits()
	fetchFestivals()
)

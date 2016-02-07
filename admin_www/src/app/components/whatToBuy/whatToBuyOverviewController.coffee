whatToBuy.controller('whatToBuyOverviewController', ($scope, $state,
	orderProductService, festivalService, $stateParams, stockUnitService) ->

	$scope.error = false

	fetchAvailiableStockUnits = () ->
		getStockUnits = stockUnitService.getList({
			'availiable': true
		})
		getStockUnits.then((response) ->
			$scope.stockUnits = response
		)
		getStockUnits.catch((response) ->
			$scope.error = true
		)

	fetchOrderProducts = (festivalId) ->
		getOrderProducts = orderProductService.getList({
			'festival-id': festivalId
		})
		getOrderProducts.then((response) ->
			$scope.orderProducts = response
		)
		getOrderProducts.catch((response) ->
			$scope.error = true
		)

	setSelectedFestival = () ->
		if $stateParams['festival-id']
			for festival in $scope.festivals
				if parseInt(festival.id) == parseInt($stateParams['festival-id'])
					$scope.selectedFestival = festival

	fetchFestivals = () ->
		getFestivals = festivalService.getList()
		getFestivals.then((response) ->
			$scope.festivals = response
			setSelectedFestival()
		)
		getFestivals.catch((response) ->
			$scope.error = true
		)

	$scope.updateSelectedFestival = (festival, something) ->
		$state.go('base.whatToBuy.overview', {'festival-id': festival.id}, {reload: true})

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
	fetchOrderProducts($stateParams['festival-id'])
	fetchAvailiableStockUnits()
	fetchFestivals()
)

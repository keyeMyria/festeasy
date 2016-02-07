whatToBuy.controller('whatToBuyOverviewController', ($scope, $state, $q,
	orderProductService, festivalService, $stateParams, stockUnitService
	psuService, productService) ->

	$scope.error = false
	festivalId = $stateParams['festival-id']

	$scope.updateSelectedFestival = (festival, something) ->
		$state.go('base.whatToBuy.overview', {'festival-id': festival.id}, {reload: true})

	ps = productService.getList()
	ops = orderProductService.getList({'festival-id': festivalId})
	sus = stockUnitService.getList({'availiable': true})
	psus = psuService.getList({'festival-id': festivalId})

	# TODO: Learn map and reduce
	meh = (ops) ->
		result = {}
		for op in ops
			pid = op.product.id
			if result[pid]
				result[pid] += op.quantity
			else
				result[pid] = op.quantity
		return result

	meh2 = (sus) ->
		result = {}
		for su in sus
			pid = su.product.id
			if result[pid]
				result[pid] += 1
			else
				result[pid] = 1
		return result

	meh3 = (psus) ->
		result = {}
		for psu in psus
			pid = psu.stock_unit.product.id
			if result[pid]
				result[pid] +=1
			else
				result[pid] = 1
		return result

	$q.all([ps, ops, sus, psus]).then((response) ->
		data = []
		[ps, ops, sus, psus] = response
		demandByProductId = meh(ops)
		availiableStockUnitsByProductId = meh2(sus)
		packagedStockUnitsByProductId = meh3(psus)
		for p in ps
			if demandByProductId[p.id]
				data.push({
					'productName': p.name || 0
					'demand': demandByProductId[p.id] || 0
					'availiableStockUnits': availiableStockUnitsByProductId[p.id] || 0
					'packagedStockUnits': packagedStockUnitsByProductId[p.id] || 0
					'toBuy': (demandByProductId[p.id] || 0) - (packagedStockUnitsByProductId[p.id] || 0) - (availiableStockUnitsByProductId[p.id] || 0)
				})
		$scope.data = data
	)

	f = festivalService.getList()
	f.then((response) ->
		$scope.festivals = response
		if $stateParams['festival-id']
			for festival in $scope.festivals
				if parseInt(festival.id) == parseInt($stateParams['festival-id'])
					$scope.selectedFestival = festival
	)
)

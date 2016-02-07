orders.controller('orderController', ($scope, $stateParams, orderService, $q,
    $state, ngNotify, packageService, orderProductService, psuService,
    productService) ->

  orderId = $stateParams.orderId
  getOrder = orderService.one(orderId).get()
  getOrder.then((response) ->
    $scope.order = response
  )
  fetchPackages = () ->
    getPackages = packageService.getList({'order-id': orderId})
    getPackages.then((response) ->
      $scope.packages = response
    )
  fetchPackages()

  meh = (psus) ->
    result = {}
    for psu in psus
      pid = psu.stock_unit.product.id
      if result[pid]
        result[pid] += 1
      else
        result[pid] = 1
    return result

  meh2 = (ops) ->
    result = {}
    for op in ops
      pid = op.product.id
      if result[pid]
        result[pid] += op.quantity
      else
        result[pid] = op.quantity
    return result
  fetchData = () ->
    ops = orderProductService.getList({'order-id': orderId})
    psus = psuService.getList({'order-id': orderId})
    ps = productService.getList()

    $q.all([ps, ops, psus]).then((response) ->
      data = []
      [ps, ops, psus] = response
      orderProductsByProductId = meh2(ops)
      packagedStockUnitsByProductId = meh(psus)
      for p in ps
        if orderProductsByProductId[p.id] || packagedStockUnitsByProductId[p.id]
          data.push({
            'productId': p.id
            'productName': p.name
            'demand': orderProductsByProductId[p.id] || 0
            'packaged': packagedStockUnitsByProductId[p.id] || 0
            'toPack': (orderProductsByProductId[p.id] || 0) - (packagedStockUnitsByProductId[p.id] || 0)
          })
      $scope.data = data
    )
  fetchData()

  $scope.deletePackage = (p) ->
    deletePackage = packageService.one(p.id).remove()
    deletePackage.then((response) ->
      ngNotify.set('Successfully deleted package.')
    )
    deletePackage.catch((response) ->
      ngNotify.set('Failed to delete package.', 'error')
    )
    deletePackage.finally((response) ->
      fetchData()
      fetchPackages()
    )

  $scope.createPackage = () ->
    params = {
      'order_id': $scope.order.id
    }
    createPackage = packageService.post(params)
    createPackage.then((response) ->
      ngNotify.set('Successfully created package for order.')
      $state.go('base.packages.package', {'packageId': response.id})
    )
    createPackage.catch((response) ->
      ngNotify.set('Failed to create package for order.', 'failed')
    )
)

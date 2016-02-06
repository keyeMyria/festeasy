orders.controller('orderController', ($scope, $stateParams, orderService, $state, ngNotify,
  packageService, orderProductService) ->
  orderId = $stateParams.orderId
  getOrder = orderService.one(orderId).get()
  getOrder.then((response) ->
    $scope.order = response
  )
  getPackages = packageService.getList({'order-id': orderId})
  getPackages.then((response) ->
    $scope.packages = response
  )
  getOrderProducts = orderProductService.getList({'order-id': orderId})
  getOrderProducts.then((response) ->
    $scope.orderProducts = response
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

orders.controller('orderController', ($scope, $stateParams, orderService, packageService, orderProductService) ->
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
)

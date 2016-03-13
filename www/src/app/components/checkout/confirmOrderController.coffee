checkout.controller('confirmOrderController', (
    orderService, $scope, $state, $stateParams, orderProductService) ->
  orderId = $stateParams['order-id']
  getOrder = orderService.one(orderId).get()
  getOrder.then((response) ->
    $scope.order = response
    orderProductService.getList({'order-id': orderId}).then((response) ->
      $scope.orderProducts = response
    )
  )
)

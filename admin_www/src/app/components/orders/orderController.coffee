orders.controller('orderController', ($scope, $stateParams, orderService) ->
  orderId = $stateParams.orderId
  getOrder = orderService.one(orderId).get()
  getOrder.then((response) ->
    $scope.order = response
  )
)

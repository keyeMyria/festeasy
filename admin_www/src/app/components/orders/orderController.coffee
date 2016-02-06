orders.controller('orderController', ($scope, $stateParams, orderService, packageService) ->
  orderId = $stateParams.orderId
  getOrder = orderService.one(orderId).get()
  getOrder.then((response) ->
    $scope.order = response
  )
  getPackages = packageService.getList({order_id: orderId})
  getPackages.then((response) ->
    $scope.packages = response
  )
)

orders.controller('ordersOverviewController', ($scope, orderService) ->
  getOrders = orderService.getList()
  getOrders.then((response) ->
    $scope.orders = response
  )
)

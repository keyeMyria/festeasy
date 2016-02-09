orders.controller('ordersOverviewController', ($scope, orderService,
    NgTableParams) ->

  getOrders = orderService.getList()
  getOrders.then((response) ->
    $scope.orders = response
    $scope.tableParams = new NgTableParams({}, { dataset: $scope.orders})
  )
)

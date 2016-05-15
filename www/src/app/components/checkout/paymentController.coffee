checkout.controller('paymentController', ($scope, $state, $stateParams, orderService, payUSetTransaction) ->
  orderId = $stateParams['order-id']
  getOrder = orderService.one(orderId).get()
  getOrder.then((response) ->
    $scope.order = response
    # Hack to get latest invoice.
    $scope.invoice = response.invoices.slice(-1).pop()
  )
  $scope.makePayment = () ->
    setTransaction = payUSetTransaction.one().get({'invoice-id': $scope.invoice.id})
    setTransaction.then((response) ->
      window.location.href = 'https://staging.payu.co.za/rpp.do?PayUReference=' + response.payu_reference
    )
)

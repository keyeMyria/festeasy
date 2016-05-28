checkout.controller('paymentController', ($scope, $state, $stateParams, orderService, payUSetTransaction) ->
  orderId = $stateParams['order-id']
  getOrder = orderService.one(orderId).get()
  getOrder.then((response) ->
    $scope.order = response
  )
  $scope.makePayment = () ->
    # TODO: Use post.
    setTransaction = payUSetTransaction.one().get({'invoice-id': $scope.order.current_invoice.id})
    setTransaction.then((response) ->
      window.location.href = 'https://staging.payu.co.za/rpp.do?PayUReference=' + response.payu_reference
    )
)

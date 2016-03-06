checkout.controller('paymentController', ($scope, $state, $stateParams) ->
  orderId = $stateParams['order-id']
  console.log orderId
)

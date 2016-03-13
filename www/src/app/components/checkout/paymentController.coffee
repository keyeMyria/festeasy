checkout.controller('paymentController', ($scope, $state, $stateParams) ->
  orderId = $stateParams['order-id']
  $scope.makeFakePayment = () ->
    console.log 'making fake payment.'
    $state.go('base.checkout.confirm-order', {'order-id': orderId})
)

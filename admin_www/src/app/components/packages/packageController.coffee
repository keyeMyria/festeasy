packages.controller('packageController', ($scope, $stateParams, packageService) ->
  packageId = $stateParams.packageId
  getPackage = packageService.one(packageId).get()
  getPackage.then((response) ->
    $scope.package = response
  )
)

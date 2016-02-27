packages.controller('packagesOverviewController', ($scope, packageService,
    NgTableParams) ->
  getPackages = packageService.getList()
  getPackages.then((response) ->
    $scope.packages = response
    $scope.packagesTableParams = new NgTableParams({}, { dataset: $scope.packages})
  )
)

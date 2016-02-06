packages.controller('packagesOverviewController', ($scope, packageService) ->
  getPackages = packageService.getList()
  getPackages.then((response) ->
    $scope.packages = response
  )
)

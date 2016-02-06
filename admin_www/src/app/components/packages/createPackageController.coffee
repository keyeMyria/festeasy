packages.controller('createPackageController', ($state, $scope, packageService, ngNotify) ->
  $scope.tp = {
    order_id: null
  }

  $scope.createPackage = (p) ->
    createPackage = packageService.post(p)
    createPackage.then((response) ->
      $scope.package = response
      ngNotify.set('Successfully created package.')
      $state.go('base.packages.package', {packageId: response.id})
    )
    createPackage.catch((response) ->
      $scope.error = true
      ngNotify.set('Failed to create package.', 'error')
    )
)

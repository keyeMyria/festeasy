packages.controller('packageController', ($scope, $stateParams, packageService,
  psuService, productService, stockUnitService, ngNotify, NgTableParams) ->

  packageId = $stateParams.packageId
  getPackage = packageService.one(packageId).get()
  getPackage.then((response) ->
    $scope.package = response
  )
  getProducts = productService.getList()
  getProducts.then((response) ->
    $scope.products = response
  )

  fetchPSUs = () ->
    getPSUs = psuService.getList({'package-id': packageId})
    getPSUs.then((response) ->
      $scope.psus = response
      $scope.tableParams = new NgTableParams({}, { dataset: $scope.psus})
    )
  fetchPSUs()

  $scope.createPSU = (packageId, stockUnitId) ->
    params = {
      'package_id': packageId,
      'stock_unit_id': stockUnitId,
    }
    createPSU = psuService.post(params)
    createPSU.then((response) ->
      $scope.selectedStockUnit = null
      fetchPSUs()
      $scope.getStockUnitByProductId($scope.selectedProduct.id)
      ngNotify.set('Successfully added product to package.')
    )
    createPSU.catch((response) ->
      ngNotify.set('Failed to add product to package', 'error')
    )

  $scope.getStockUnitByProductId = (productId) ->
    params = {
      'product-id': productId
      'available': true
    }
    getStockUnits = stockUnitService.getList(params)
    getStockUnits.then((response) ->
      $scope.stockUnits = response
    )

  $scope.removePSU = (psu) ->
    deletePSU = psuService.one(psu.id).remove()
    deletePSU.then((response) ->
      fetchPSUs()
      if $scope.selectedProduct
        $scope.getStockUnitByProductId($scope.selectedProduct.id)
      ngNotify.set('Successfully removed product.')
    )
    deletePSU.catch((response) ->
      ngNotify.set('Failed to remove product.', 'error')
    )


  $scope.updateSelectedProduct = (product, something) ->
    $scope.selectedProduct = product
    $scope.getStockUnitByProductId(product.id)

  $scope.updateSelectedStockUnit = (stockUnit, something) ->
    $scope.selectedStockUnit = stockUnit

)

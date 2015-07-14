app.factory 'productsService', ['Restangular', '$q', (Restangular, $q) ->

    fac = {}

    get_products = () =>
        deferred = $q.defer()
        Restangular.one('products').get().then (data) =>
            deferred.resolve data
        , (error) => 
            deferred.reject error
        return deferred.promise

    fac.get_products = get_products
    return fac
]

services.factory('payUSetTransaction', (Restangular) ->
	return Restangular.service('payu-transactions')
)

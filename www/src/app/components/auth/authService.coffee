auth.factory('authService', ($q, $auth) ->
	api = {}
	api.signin = (user) ->
		deferred = $q.defer()
		a = $auth.login(user)
		a.then((response) ->
			console.log $auth.getToken()
			console.log 'Singed in'
			deferred.resolve(response)
		)
		a.catch((response)->
			deferred.reject(response)
		)
		return deferred.promise
	return api
)
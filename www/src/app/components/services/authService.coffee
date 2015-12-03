services.factory('authService', ($q, $auth) ->
	api = {}
	signin = (user) ->
		deferred = $q.defer()
		a = $auth.login(user)
		a.then((response) ->
			console.log 'Singed in'
			deferred.resolve(response)
		)
		a.catch((response)->
			deferred.reject(response)
		)
		return deferred.promise
	signup = (user) ->
		deferred = $q.defer()
		a = $auth.signup(user)
		a.then((response) ->
			console.log 'Signed up'
			b = signin(user)
			b.then((response) ->
				deferred.resolve(response)
			)
			b.catch((response) ->
				deferred.reject(response)
			)
		)
		a.catch((response) ->
			deferred.reject(response)
		)
		return deferred.promise

	getAuthenticatedUser = ->
		if $auth.isAuthenticated()
			return {
				id: $auth.getPayload().sub
			}
		return null

	api.signin = signin
	api.signup = signup
	api.getAuthenticatedUser = getAuthenticatedUser
	return api
)

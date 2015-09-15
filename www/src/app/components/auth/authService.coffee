auth.factory('authService', ($auth) ->
	api = {}
	api.signin = (user) ->
		promise = $auth.login(user)
		promise.then(() ->
			console.log 'Singed in'
		)
	return api
)
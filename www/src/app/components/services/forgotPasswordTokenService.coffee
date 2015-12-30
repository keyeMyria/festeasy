services.factory('forgotPasswordTokenService', (Restangular) ->
	return Restangular.service('forgot-password-tokens')
)

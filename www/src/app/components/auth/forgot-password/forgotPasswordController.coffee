auth.controller('forgotPasswordController', ($scope, forgotPasswordTokenService, ngNotify) ->
	$scope.emailAddress = null
	$scope.sendPasswordRecoveryEmail = (emailAddress) ->
		params = {
			email_address: emailAddress
		}
		post = forgotPasswordTokenService.post(params)
		post.then((response) ->
			ngNotify.set("Successfully sent email.")
		)
		post.catch((response) ->
			ngNotify.set("Failed to send email.", 'error')
		)
)

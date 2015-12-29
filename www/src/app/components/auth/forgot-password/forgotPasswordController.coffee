auth.controller('forgotPasswordController', ($scope, forgotPasswordTokenService, ngNotify) ->
	$scope.emailAddress = null
	$scope.sendPasswordRecoveryEmail = (emailAddress) ->
		$scope.message = null
		params = {
			email_address: emailAddress
		}
		post = forgotPasswordTokenService.post(params)
		post.then((response) ->
			ngNotify.set("Successfully sent email.")
			$scope.message = 'Please check your email.'
		)
		post.catch((response) ->
			ngNotify.set("Failed to send email.", 'error')
		)
)

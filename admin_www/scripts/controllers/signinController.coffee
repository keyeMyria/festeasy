app.controller('SigninController', (userService, $scope, $state) ->
    
    $scope.signin_form = {
        is_loading: false
        is_auth_error: false
    }

    $scope.signin = (form) ->
        $scope.signin_form.is_loading = true
        $scope.signin_form.is_auth_error = false
        promise = userService.signin(
            $scope.email_address, 
            $scope.password,
        )
        promise.then () ->
            $state.go 'base.landing'
        , (error) ->
            if error.status == 401
                $scope.signin_form.is_auth_error = true
        promise.finally (data) ->
            $scope.signin_form.is_loading = false
)

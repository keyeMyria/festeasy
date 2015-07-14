app.controller('SignoutController', (userService, $scope, $state) ->

    $scope.signout = () ->
        userService.signout()
        .then () ->
            $state.go 'base.landing'
        , (error) ->
)
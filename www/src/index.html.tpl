<!DOCTYPE html>
<html data-ng-app="app" lang="en">
    <head>
        <meta charset="utf-8" />
        <base href="/">
        <meta http-equiv="X-UA-Compatible" content="IE=edge, chrome=1" />
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta http-equiv="refresh" content="3600">
        <title>FestEasy</title>
        <!-- inject:css -->
        <link href="bower.css?build_number=<%= buildNumber %>" rel="stylesheet" />
        <link href="app/assets/css/styles.css?build_number=<%= buildNumber %>" rel="stylesheet" />
        <!-- endinject -->
    </head>
    <body>
        <div ui-view></div>
        <!-- inject:js -->
        <!-- Bootstrapping -->
        <script src="bower.js?build_number=<%= buildNumber %>"></script>
        <script src="my.js?build_number=<%= buildNumber %>"></script>
        <!-- endinject -->
    </body>
</html>
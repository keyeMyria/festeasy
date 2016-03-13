# Ryan, you will want to swap these two lines around when you work on the site
# so that it works on your pc without the backend server component fow now :)
# ie: comment out line 5 by prepending a '#', and uncomment line 6 by removing the '#'

angular.module('conf', []).constant('API_END_POINT', 'http://localhost:5000/api/v1');
#angular.module('conf', []).constant('API_END_POINT', 'https://festeasy-staging.herokuapp.com/api/v1');

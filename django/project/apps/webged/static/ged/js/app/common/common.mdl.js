(function(){
    'use strict';

    angular
      .module('my-ged.common', ['restangular','ngCookies' ]	)
      .config(['RestangularProvider', function(RestangularProvider) {
           // RestangularProvider.setBaseUrl('apis/');
           // RestangularProvider.setMethodOverriders(["put", "delete"]);
        }]);

	angular
      .module('my-ged.common')
      .config(function(RestangularProvider) {
      RestangularProvider.setBaseUrl('apis/');
      //RestangularProvider.setMethodOverriders(["put", "delete"]);
      RestangularProvider.setRequestSuffix('/?format=json');
      RestangularProvider.setDefaultHeaders({'Content-Type': 'application/json'});
     // AuthRestangular.setDefaultHeaders({'Authorization': 'Token ' + $rootScope.globals.token });
      
	});

    angular
    .module('my-ged.common')
    .factory("TokenRestangular", function (Restangular, $rootScope, $cookies) {
       return Restangular.withConfig(function (RestangularConfigurer) {

        var token = $cookies.get('authtoken');
        // Setting a cookie
        //$cookies.put('myFavorite', 'oatmeal');

       // Set access token in header.
       RestangularConfigurer.setBaseUrl('apis/');
       RestangularConfigurer.setRequestSuffix('/?format=json');
       RestangularConfigurer.setDefaultHeaders({'Content-Type': 'application/json'});
       RestangularConfigurer.setDefaultHeaders({'Authorization': 'Token ' + token });

    });
})

})();
(function() {
  'use strict';
  angular
    .module('blogApp')
    .config(stateConfig);

  stateConfig.$inject = ['$stateProvider', '$urlRouterProvider'];

  function stateConfig($stateProvider, $urlRouterProvider) {
    // Redirect to home page if no other URL matches
    $urlRouterProvider.otherwise('/');

    $stateProvider.state('app', {
      abstract: true,
      views: {
        // 'headerbar@': {
        //   templateUrl: 'app/layouts/headerbar/headerbar.html',
        //       controller: 'HeaderbarController',
        //       controllerAs: 'vm'
        // },
        //   'navbar@': {
        //       templateUrl: 'app/layouts/navbar/navbar.html',
        //       controller: 'NavbarController',
        //       controllerAs: 'vm'
        //   }
      }
    });
  }
}());

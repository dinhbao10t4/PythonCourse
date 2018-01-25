(function() {
    'use strict';

    angular
        .module('blogApp')
        .config(stateConfig);

    stateConfig.$inject = ['$stateProvider'];

    function stateConfig($stateProvider) {
        $stateProvider.state('account', {
            parent: 'app',
            url: '/account',
            views: {
                'content@': {
                    templateUrl: '/static/partials/account.html',
                    controller: 'AccountController',
                    controllerAs: 'vm'
                }
            }
        });
    }
})();

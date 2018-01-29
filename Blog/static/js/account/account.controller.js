(function() {
  'use strict';

  angular.module('blogApp').controller('AccountController',
    AccountController);

  AccountController.$inject = ['$http', '$state'];

  function AccountController($http, $state) {
    var vm = this;
    vm.mode = 'login';
    vm.errorMessage = '';

    vm.changeToLoginMode = function(){
      vm.mode = 'login';
    };

    vm.changeToRegisterMode = function(){
      vm.mode = 'register';
    };

    vm.login = function() {
      $http({
        method: "POST",
        url: "http://127.0.0.1:5000/login",
        headers: {
          'Access-Control-Allow-Origin': '*',
          'Content-Type': 'application/json',
        },
        data: {
          'userName': vm.userName,
          'password': vm.password
        }
      }).then(function successCallback(response) {
        var data = response.data;
        if(data.result == 'success'){
          $state.go('blog.list', null, {
            reload : true
          });
        } else {
          vm.errorMessage = data.result;
        }
      });
    };

    vm.register = function() {
      $http({
        method: "POST",
        url: "http://127.0.0.1:5000/register",
        headers: {
          'Access-Control-Allow-Origin': '*',
          'Content-Type': 'application/json',
        },
        data: {
          'userName': vm.userName,
          'password': vm.password
        }
      }).then(function successCallback(response) {
        vm.userName = '';
        vm.password = '';
        $state.go('account', null, {
          reload : true
        });
      });
    };
  }
}());

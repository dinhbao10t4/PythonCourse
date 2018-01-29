(function() {
  'use strict';

  angular.module('blogApp').controller('BlogCreateUpdateController',
    BlogCreateUpdateController);

  BlogCreateUpdateController.$inject = ['$http', 'entity', '$state'];

  function BlogCreateUpdateController($http, entity, $state) {
    var vm = this;
    vm.blog = entity;
    vm.init = init;
    vm.init();

    function init(){
      if(vm.blog.id){
        $http({
          method: "POST",
          url: "http://127.0.0.1:5000/get-one-blog",
          headers: {
            'Access-Control-Allow-Origin': '*',
            'Content-Type': 'application/json',
          },
          data: {'id': vm.blog.id}
        }).then(function successCallback(response) {
          vm.blog = response.data;
        });
      }
    }

    vm.isUpdate = function(){
      if(vm.blog.id){
        return true;
      } else {
        return false;
      }
    };

    vm.createBlog = function(){
      $http({
        method: "POST",
        url: "http://127.0.0.1:5000/blog",
        headers: {
          'Access-Control-Allow-Origin': '*',
          'Content-Type': 'application/json',
        },
        data: vm.blog
      }).then(function successCallback(response) {
        $state.go('blog.list', null, {
          reload : true
        });
      });
    }

    vm.updateBlog = function(){
      $http({
        method: "POST",
        url: "http://127.0.0.1:5000/update-blog",
        headers: {
          'Access-Control-Allow-Origin': '*',
          'Content-Type': 'application/json',
        },
        data: vm.blog
      }).then(function successCallback(response) {
        $state.go('blog.list', null, {
          reload : true
        });
      });
    }

    vm.logout = function(){
      $http({
        method: "GET",
        url: "http://127.0.0.1:5000/logout",
        headers: {
          'Access-Control-Allow-Origin': '*',
          'Content-Type': 'application/json',
        },
        data: {}
      }).then(function successCallback(response) {
        var data = response.data;
        if(data.result == 'logout'){
          $state.go('account', null, {
            reload : true
          });
        }
      });
    };
  }
}());

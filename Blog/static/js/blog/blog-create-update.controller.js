(function() {
  'use strict';

  angular.module('blogApp').controller('BlogCreateUpdateController',
    BlogCreateUpdateController);

  BlogCreateUpdateController.$inject = ['$http', 'entity'];

  function BlogCreateUpdateController($http, entity) {
    var vm = this;
    vm.blog = entity;
    console.log(vm.blog);

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
        console.log(response);
      });
    }
  }
}());

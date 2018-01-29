(function() {
  'use strict';

  angular.module('blogApp').controller('BlogDetailController',
    BlogDetailController);

  BlogDetailController.$inject = ['$http', 'blogId', '$state'];

  function BlogDetailController($http, blogId, $state) {
    var vm = this;
    vm.blogId = blogId;
    vm.init = init;
    vm.init();

    function init(){
      if(vm.blogId){
        $http({
          method: "POST",
          url: "http://127.0.0.1:5000/get-one-blog",
          headers: {
            'Access-Control-Allow-Origin': '*',
            'Content-Type': 'application/json',
          },
          data: {'id': vm.blogId}
        }).then(function successCallback(response) {
          vm.blog = response.data;
        });
      }
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

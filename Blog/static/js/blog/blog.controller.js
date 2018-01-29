(function() {
  'use strict';

  angular.module('blogApp').controller('BlogController',
    BlogController);

  BlogController.$inject = ['$http', '$state'];

  function BlogController($http, $state) {
    var vm = this;
    vm.init = init;
    vm.getAllBlog = getAllBlog;
    vm.getYourBlog = getYourBlog;
    vm.blogs = [];
    vm.isEdit = false;
    vm.entries = 5;
    vm.page = 1;
    vm.sizePerPages = [5, 10, 25];
    vm.isAllBlog = true;
    vm.totalPage = 0;
    vm.init();

    function init(){
      vm.getAllBlog();
    }

    vm.randomImage = function(id){
      var imageArr = ['bg0.jpg','bg5.jpg','bg7.jpg','bg9.jpg',
      'bg10.jpg','bg12.jpg'];
      return imageArr[Math.floor((id % imageArr.length))];
    };

    vm.transition = function(){
      vm.page = 1;
      if(vm.isAllBlog){
        vm.getAllBlog();
      } else {
        vm.getYourBlog();
      }
    };

    vm.previousPage = function(){
      if(vm.page - 1 >= 1){
        vm.page = vm.page - 1;
        if(vm.isAllBlog){
          vm.getAllBlog();
        } else {
          vm.getYourBlog();
        }
      }
    };

    vm.nextPage = function(){
      if(vm.page + 1 <= vm.totalPage){
        vm.page = vm.page + 1;
        if(vm.isAllBlog){
          vm.getAllBlog();
        } else {
          vm.getYourBlog();
        }
      }
    };

    vm.changePage = function(page){
      vm.page = page;
      if(vm.isAllBlog){
        vm.getAllBlog();
      } else {
        vm.getYourBlog();
      }
    };

    function onSuccess(response){
      var data = response.data;
      vm.pageLst = [1];
      if(data.result.length){
        vm.blogs = data.result;
        vm.totalPage = Math.ceil((data.totalRow / vm.entries));
        if(vm.totalPage > 1){
          for(var i = 2; i <= vm.totalPage; i++){
            vm.pageLst.push(i);
          }
        }
      } else {
        vm.blogs = [];
        vm.totalPage = 0;
      }
    }

    vm.enterAllBlog = function(){
      vm.isAllBlog = true;
      vm.getAllBlog();
    };

    vm.enterYourBlog = function(){
      vm.isAllBlog = false;
      vm.enterYourBlog();
    }

    function getAllBlog(){
      vm.blogs = [];
      vm.isEdit = false;
      $http({
        method: "POST",
        url: "http://127.0.0.1:5000/all-blog",
        headers: {
          'Access-Control-Allow-Origin': '*',
          'Content-Type': 'application/json',
        },
        data: {
          per_page: vm.entries,
          page: vm.page
        }
      }).then(function successCallback(response) {
        onSuccess(response);
      });
    };

    function getYourBlog(){
      vm.isEdit = true;
      vm.blogs = [];
      $http({
        method: "POST",
        url: "http://127.0.0.1:5000/your-blog",
        headers: {
          'Access-Control-Allow-Origin': '*',
          'Content-Type': 'application/json',
        },
        data: {
          per_page: vm.entries,
          page: vm.page
        }
      }).then(function successCallback(response) {
        onSuccess(response);
      });
    };

    vm.deletePost = function(id){
      $http({
        method: "POST",
        url: "http://127.0.0.1:5000/delete-one-blog",
        headers: {
          'Access-Control-Allow-Origin': '*',
          'Content-Type': 'application/json',
        },
        data: {'id': id}
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

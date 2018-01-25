(function() {
  'use strict';

  angular.module('blogApp').controller('BlogController',
    BlogController);

  BlogController.$inject = ['$http'];

  function BlogController($http) {
    var vm = this;
  }
}());

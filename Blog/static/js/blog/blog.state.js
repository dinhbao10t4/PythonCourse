(function() {
  angular
  .module('blogApp')
  .config(stateAbsConfig)
  .config(stateConfig);

  stateAbsConfig.$inject = ['$stateProvider'];

  function stateAbsConfig($stateProvider) {
      $stateProvider.state('blog', {
        url: '/blog',
          abstract: true,
          parent: 'app'
      });
  }

  stateConfig.$inject = ['$stateProvider'];

  function stateConfig($stateProvider) {
    $stateProvider
    .state('blog.list', {
        parent: 'blog',
        url: '/list',
        views: {
            'content@': {
                templateUrl: '/static/partials/blog.html',
                controller: 'BlogController',
                controllerAs: 'vm'
            }
        },
        params: {
        },
        resolve: {
        }
    }).state('blog.new', {
          parent : 'blog',
          url : '/new',
          views : {
            'content@' : {
              templateUrl : '/static/partials/create-update-blog.html',
              controller : 'BlogCreateUpdateController',
              controllerAs : 'vm'
            }
          }, params: {
          }, resolve : {
            entity : function() {
              return {
                title : null,
                content : null,
              };
            }
          }
        });
  }
}());

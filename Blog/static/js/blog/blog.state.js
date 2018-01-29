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
    })
    .state('blog.detail', {
          parent : 'blog',
          url : '/{id}/detail',
          views : {
            'content@' : {
              templateUrl : '/static/partials/detail-blog.html',
              controller : 'BlogDetailController',
              controllerAs : 'vm'
            }
          }, params: {
          }, resolve : {
            blogId : function($stateParams) {
              return $stateParams.id;
            }
          }
        })
    .state('blog.new', {
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
        })
    .state('blog.edit', {
          parent : 'blog',
          url : '/{id}/edit',
          views : {
            'content@' : {
              templateUrl : '/static/partials/create-update-blog.html',
              controller : 'BlogCreateUpdateController',
              controllerAs : 'vm'
            }
          }, params: {
          }, resolve : {
            entity : function($stateParams) {
              return {
                id: $stateParams.id,
                title : null,
                content : null,
              };
            }
          }
        });
  }
}());

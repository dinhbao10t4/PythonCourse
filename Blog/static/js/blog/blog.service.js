(function() {
  'use strict';
  angular.module('blogApp').factory('Blog', Blog);

	Blog.$inject = [ '$resource' ];

	function Blog($resource) {
		var resourceUrl = 'http://127.0.0.1:5000/blog/:id';

		return $resource(resourceUrl, {}, {
			'query' : {
				method : 'GET',
				isArray : true
			},
			'get' : {
				method : 'GET',
				transformResponse : function(data) {
					data = angular.fromJson(data);
					return data;
				}
			},
			'update' : {
				method : 'PUT'
			},
			'save' : {
				method : 'POST'
			},
			'delete' : {
				method : 'DELETE'
			}
		});
	}
}());

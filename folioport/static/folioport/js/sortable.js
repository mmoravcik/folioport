folioport = window.folioport || {};

(function () {
	'use strict';
		folioport.setupSortables = function() {
		// TODO do some DRY in this script tag
		var sortableGroup = $('ol.sortable').sortable({
			onDrop: function (item, container, _super) {
				var data = sortableGroup.sortable("serialize").get();
				var itemOrder = [];
				for(var i = 0; i < data[0].length; i++) {
					var obj = data[0][i];
					itemOrder.push(obj.id);
				}
				var data = JSON.parse('{"item_order": "'+ itemOrder +'"}');
				$.post(folioport.urls.itemOrderSaveUrl, data, function( data ) {
					if (data.status == 'success') {
						$.growl.notice({'message': 'Order of your items has been saved'});
					} else {
						alert('Sorry! Unable to save your order :(');
					}
				});
				_super(item, container)
			}
		});

		var sortableTableGroup = $('table.sorted-table').sortable({
			containerSelector: 'table',
			itemPath: '> tbody',
			itemSelector: 'tr',
			placeholder: '<tr class="placeholder"/>',
			onDrop: function (item, container, _super) {
				var data = sortableTableGroup.sortable("serialize").get();
				var itemOrder = [];
				for(var i = 0; i < data[0].length; i++) {
					var obj = data[0][i];
					itemOrder.push(obj.id);
					var objectType = obj.object;
					if (obj.hasOwnProperty('app')) {
						var objectApp = obj.app;
					}
				}
				var data = JSON.parse('{"item_order": "'+ itemOrder +'"}');
				if (objectType == 'project') {
					var url = folioport.urls.projectOrderSaveUrl;
				} else if (objectType == 'page') {
					var url = folioport.urls.pageOrderSaveUrl;
				} else {
					var url = folioport.urls.categoryOrderSaveUrl;
					url = url.replace('replace', objectApp);
				}
				$.post(url, data, function( data ) {
					if (data.status == 'success') {
						$.growl.notice({'message': 'Order of your items has been saved'});
					} else {
						alert('Sorry! Unable to save your order :(');
					}
				});
				_super(item, container)
			}
		});
	};

	folioport.setupSortables();

}());

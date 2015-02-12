folioport = window.folioport || {};

(function () {
	'use strict';

	folioport.main = function() {
		folioport.setupDatePicker();
		folioport.setupImageHovers();
		folioport.setupToggleMenu();
	};

	folioport.setupDatePicker = function() {
	    $(".cms_date_field").each(function() {
			$(this).datetimepicker({
				timepicker: false,
				format: 'd/m/Y'
			});
    	});
	};

	folioport.setupImageHovers = function() {
	    $(".image-container").has('.hover_image').hover(function() {
			$(this).find(".normal_image").hide();
			$(this).find(".hover_image").show();

			}, function() {
				$(this).find(".hover_image").hide();
				$(this).find(".normal_image").show();
		});
	};

	folioport.setupToggleMenu = function() {
	    $("#menu-toggle").click(function(e) {
			e.preventDefault();
			$("#wrapper").toggleClass("toggled");
		});
	};

	folioport.main();
}());


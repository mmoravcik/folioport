module.exports = function(grunt) {
	var path = require('path');

	require('load-grunt-config')(grunt, {
		config: {
			configPath: path.join(process.cwd(), 'folioport/grunt'),
			build: 'staticfiles',
			ui: 'folioport/static',
			templates: 'folioport/templates'
		}
	});
};
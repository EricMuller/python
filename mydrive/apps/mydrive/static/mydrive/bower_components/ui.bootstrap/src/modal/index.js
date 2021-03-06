require('../stackedMap');
require('../../template/modal/backdrop.html.js');
require('../../template/modal/window.html.js');
require('./modal');
require('../position/position.css');

var MODULE_NAME = 'ui.bootstrap.module.modal';

angular.module(MODULE_NAME, ['ui.bootstrap.modal', 'uib/template/modal/backdrop.html', 'uib/template/modal/window.html']);

module.exports = MODULE_NAME;

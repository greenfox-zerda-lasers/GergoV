'use strict';

var test = require('tape');
var appendA = require('./40.js');

test('Test appendA() function', function(t) {
  var actual = appendA('alm');
  var expected = 'alma';

  t.equal(actual, expected);
  t.end();
});

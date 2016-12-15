'use strict';

var test = require('tape');
// ! Need exact path:
var unit = require('./39.js')


// test

test('Double input value', function(t) {
  var actual = unit(23);
  var expected = 46;

  t.equal(actual, expected);
  t.end();
});

test('Throw exception if input is not a number', function(t) {
  t.throws(function (){
    unit('kutya');
  }, TypeError);
  t.end();
});

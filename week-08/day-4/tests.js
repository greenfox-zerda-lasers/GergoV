'use strict';

var test = require('tape');
var doubleIt = require('./39.js')
var appendA = require('./40.js');
var numAdder = require('./41.js');
var calcFactorial = require('./42.js');
var filterOdd = require('./43.js');
var myMin = require('./44.js');
var shortestName = require('./45.js');

// Test 39.js

test('Testing doubleIt() basic functionality:', function(t) {
  var actual = doubleIt(23);
  var expected = 46;

  t.equal(actual, expected);
  t.end();
});

test('Throw exception if input is not a number', function(t) {
  t.throws(function (){
    doubleIt('kutya');
  }, TypeError);
  t.end();
});

// Test 40.js

test('Testing appendA() basic functionality:', function(t) {
  var actual = appendA('alm');
  var expected = 'alma';

  t.equal(actual, expected);
  t.end();
});

// Test 41.js

test('Testing numAdder() basic functionality:', function(t) {
  var actual = numAdder([1, 1, 1, 1]);
  var expected = 4;

  t.equal(actual, expected);
  t.end();
});

// Test 42.js

test('Testing calcFactorial() basic functionality:', function(t) {
  var actual = calcFactorial(5);
  var expected = 120;

  t.equal(actual, expected);
  t.end();
});

// Test 43.js

test('Testing filterOdd() basic functionality:', function(t) {
  var actual = filterOdd([1, 2, 3, 4, 5, 6]);
  var expected = [2, 4, 6];

  t.deepEqual(actual, expected);
  t.end();
});

// Test 44.js

test('Testing myMin() basic functionality:', function(t) {
  var actual = myMin([3, 7, -1, 99, -7, 5, 2]);
  var expected = -7;

  t.equal(actual, expected);
  t.end();
});

// Test 45.js

test('Testing shortestName() basic functionality:', function(t) {
  var actual = shortestName(['Zakarias', 'Hans', 'Otto', 'Ole']);
  var expected = 'Ole';

  t.deepEqual(actual, expected);
  t.end();
});

// Testing callback functions by creating own universal fct

'use strict';

let addEm = function(a, b) {
  return a + b;
};

let multEm = function(a, b) {
  return a*b;
};

let tellEm = function(a, b) {
  console.log(`Here are your two numbers: ${a}, ${b}`);
}

var calcIt = function(num1, num2, callback) {
    return callback(num1, num2);
};

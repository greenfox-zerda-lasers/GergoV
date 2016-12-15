'use strict';

// create a function that returns it's input factorial

function calcFactorial(input) {
  var fact = 1
  for (var i = 1; i <= input; i++) {
    fact *= i
  }
  return fact
}

var out = calcFactorial(5);
console.log(out)

module.exports = calcFactorial;

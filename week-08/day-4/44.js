'use strict';

var numbers = [7, 5, 8, -1, 2];
// Write a function that returns the minimal element
// in an array (your own min function)

function myMin(input) {
  var minimal = input[0];
  for (var i=0; i < input.length-1; i++) {
    if (minimal > input[i + 1]) { minimal = input[i]}
  };
  return minimal;
};

var out = myMin(numbers);
console.log(out);

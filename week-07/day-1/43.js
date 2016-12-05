'use strict';

var numbers = [3, 4, 5, 6, 7];
// write a function that filters the odd numbers
// from an array and returns a new array consisting
// only the evens

function filterOdd(list) {
  var evens = [];
  for (var i=0; i < list.length; i++) {
    if (list[i] % 2 == 0) {
      evens.push(list[i]);
    }
  }
  return evens
}

console.log(filterOdd(numbers))

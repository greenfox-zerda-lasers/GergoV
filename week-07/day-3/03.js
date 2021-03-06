'use strict';

// write a function called each that takes an array and a function as a paramter
// and calls the function with each element of the array as parameter
// so it should call the array 3 times if the array has 3 elements

function each (arr, func) {
  arr.forEach(function(element, index, array) { func(element, index, array) } );
};

function each (arr, func) {
  arr.forEach(func);
};

each(['Apple', 'Pen', 'Pinepplepen'], console.log)

'use strict';

var numbers = [2, 5, 11, 29];

// create a function that takes an array of numbers and returns a boolean
// it should return true if all the elements are prime, false otherwise

// solution via Levi

function rPrimes(arr) {
 return arr.every(function (e) {
   for (var j = 2, stop = Math.floor(Math.sqrt(e)); j <= stop;  j++) {
     if (e % j === 0) {
       return false;
     };
   };
   return true;
 });
};

// default output line

var out = rPrimes(numbers);
console.log(out);

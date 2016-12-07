'use strict';

var numbers = [2, 5, 11, 29];

// create a function that takes an array of numbers and returns a boolean
// it should return true if all the elements are prime, false otherwise


function examineArray(arr) {
  var isItPrime = function(e) {
    var isprime = true;
    for (var i = 2; i <= Math.sqrt(e); i++) {
      if (e % i === 0) {
        isprime = false;
        };
      };
    return isprime;
    };

  var areTheyPrime = arr.map(isItPrime);

  var areTheyAllPrime = areTheyPrime.every(function(e){
    return e == true;
  });
};

var out  = examineArray(numbers);
console.log(out);

'use strict';

// create a function that takes a string and counts its letters
// it should return an object thats keys are the letters and the values are
// the counts.
// example: "apple" -> {a: 1, p: 2, l: 1, e: 1}

function countLettersReduce(text) {
  var arr = text.split('');
  return arr.reduce(function(acc, char) {
    acc[char] = (acc[char]+1) || 1;
    return acc;
  }, {});
};

console.log(countLettersReduce('applepen'));

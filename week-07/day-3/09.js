'use strict';

// create a function that takes a string and counts its letters
// it should return an object thats keys are the letters and the values are
// the counts.
// example: "apple" -> {a: 1, p: 2, l: 1, e: 1}


function countLetters(text) {
  var textArray = text.split('');
  var out = {};
  textArray.forEach(function(e) {
    if (out[e] == undefined) {
      out[e] = 1;
    } else {
      out[e]++;
    };
  });
  return out;
};

console.log(countLetters('apple'));

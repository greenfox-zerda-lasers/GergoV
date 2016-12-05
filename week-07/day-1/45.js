
'use strict';

var names = ['Zakarias', 'Hans', 'Otto', 'Ole'];
// create a function that returns the shortest string
// from an array

function shortestName(input) {
  var shortest = input[0];
  for (var i=0; i < input.length-1; i++) {
    if (shortest.length > input[i + 1].length) { shortest = input[i + 1] };
  };
  return shortest;
};

var out = shortestName(names);
console.log(out);

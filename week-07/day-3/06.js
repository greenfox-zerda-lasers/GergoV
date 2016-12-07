'use strict';


// create a function that takes a string and a letter and returns a boolean
// it should return true if the string consits the given letter, false otherwise

function isItInThere (string, letter) {
  if (string.indexOf(letter) > -1) {
    return true;
  }
  else {
    return false;
  }
}

var out = isItInThere('Alma', 'a');
console.log(out)

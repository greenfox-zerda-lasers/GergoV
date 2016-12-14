
// Create a "tour" function that takes two functions as parameters:
//  - walk and distance
//  - distance should return an array of false values [false,false,false] with the length of a given parameter
//  - walk should go through the returned array of distance and change it to true
//  - tour should return the result of walk

function tour(walk, distance) {
};

function distance(a) {
  var arrOut = Array(a);
  for (i=0; i<arrOut.length; i++) {
    arrOut[i] = false;
  };
  return arrOut;
};

function walk(array) {
  array.forEach(function(e) {
    e = true;
  });
  return array;
};

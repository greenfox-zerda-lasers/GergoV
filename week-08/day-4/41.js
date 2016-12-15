'use strict';

var numbers = [4, 5, 6, 7, 8, 9, 10]
// write your own sum function

function numAdder(nums) {
  var added = 0;
  for (var i = 0; i < nums.length; i++) {
    added += nums[i]
  }
  return added
}

console.log(numAdder(numbers))

module.exports = numAdder;

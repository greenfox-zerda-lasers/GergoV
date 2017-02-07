function binarysearch(array, n) {
  let sampleArray = array;

  // Set l to array length
  let l = sampleArray.length;

  if (l == 1 && sampleArray[0] != n)  {
    console.log("Array doesn't have the element.");
    return false;
  }
  if (l == 1 && sampleArray[0] == n)  {
    console.log("Array has the element.");
    return true;
  }

  // Find middle element of array
  let halfLength = l/2;
  // round if odd
  let targetIndex;
  if (halfLength % 2 > 0) {
    targetIndex = (halfLength * 10 / 10) - ((halfLength * 10 % 10) / 10);
  } else {
    targetIndex = halfLength;
  }

  let x = sampleArray[targetIndex];
  console.log("Looking sample array: ", sampleArray, " of length: ", l, "; Splitting by: ", x);

  if (x == n) {
    console.log("Array has number.");
    return true;
  }
  let sampleArrayHalf = [];
  if (x < n) {
    for (i=targetIndex+1; i < l; i++) {
      sampleArrayHalf.push(sampleArray[i]);
    }
  }
  if (x > n) {
    for (i=0; i < targetIndex-1; i++) {
      sampleArrayHalf.push(sampleArray[i]);
    }
  }
  binarysearch(sampleArrayHalf, n);
};

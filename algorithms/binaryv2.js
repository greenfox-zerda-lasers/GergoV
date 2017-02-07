function binarySearch(array, n) {
  var middleIndex = Math.floor(array.length / 2);
  var middleElement = array[middleIndex];
  console.log("Array: ", array, ", middleElement: ", middleElement);

  if (array.length == 1 && middleElement != n) {
    console.log("We are out of array and N is not in array.");
    return false;
  }

  if (middleElement == n) {
    console.log("N is in array.");
    return true;
  } else if (middleElement < n) {
    array.splice(0, middleIndex + 1);
    console.log("x < n;");
    return binarySearch(array, n);
  } else if (middleElement > n) {
    array.splice(middleIndex, (array.length -1));
    console.log("x > n;");
    return binarySearch(array, n);
  } else {
    console.log("N is not in array.");
    return false;
  }
};

// 0 1 2 3 4 -> floor(5/2) = 2
// 0 1 2 3   -> 2

// 0 1 -> 1.

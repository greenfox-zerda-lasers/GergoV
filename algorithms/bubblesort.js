let myArray = [4, 7, 9, 11, 2, 1, 0, 8];

function bubbleSort (a) {
	let isSorted;
	do {
		isSorted = true;
		console.log(a);
		for (var i=0; i < a.length - 1; i++) {
			if (a[i] > a[i+1]) {
				let temp = a[i];
				a[i] = a[i+1];
				a[i+1] = temp;
				isSorted = false;
			} 
		}; 
	} while (isSorted == false);
	console.log("Final: ", a);
};

bubbleSort(myArray);
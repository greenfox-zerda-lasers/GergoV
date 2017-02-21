// Find the sum of all the multiples of 3 or 5 below 1000.

let multiples = [];

for (i=0; i<=1000; i++) {
	if (i % 3 == 0 || i % 5 == 0) {
		multiples.push(i);
	} 
}

let sum = 0;
for (j=0; j<multiples.length-1; j++) {
	sum += multiples[j];
}

console.log("Sum of all: ", sum);

// Even Fibonacci below 4M;

let sum = 0;
let fibonaccis = [];

// Calculate Fibonacci sequence till top value
function fibonacciSeq(topValue) {
  for (var i=0;i<topValue;i++) {
    if (i === 0) {
      fibonaccis.push(0);
    }
    else if (i === 1) {
      fibonaccis.push(1);
    }
    else if (fibonaccis[i-1] + fibonaccis[i-2] <= topValue){
      fibonaccis.push(fibonaccis[i-1] + fibonaccis[i-2]);
    } else {
      break;
    }
  }
};

fibonacciSeq(4000000);

var evenFibonaccis = [];

for (i=0;i<fibonaccis.length;i++) {
  if (fibonaccis[i] % 2 == 0) {
    evenFibonaccis.push(fibonaccis[i]);
  }
}

console.log(evenFibonaccis);

for (i=0;i<evenFibonaccis.length;i++) {
  sum += evenFibonaccis[i];
}

console.log(sum);

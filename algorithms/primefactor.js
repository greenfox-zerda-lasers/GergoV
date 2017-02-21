// What is the largest prime factor of the number 600851475143 ?

var val = 600851475143;
var primes = [];
var primeFactors = [];

// Find primes up to sqrt(val)
val = 100000;

for (var i = 2; i <= Math.floor(Math.sqrt(val)); i++) {
  var isPrime = true;
  for (var j = 2; j <= Math.floor(Math.sqrt(i)); j++) {
    if (i % j === 0) {
      isPrime = false;
    }
    if (isPrime === true) {
      primes.push(i);
    }
  }
}

console.log("Primes up to sqrt: " + primes);

for (var k = 0; k <= primes.length; k++) {
  if (val % primes[k] === 0) {
    primeFactors.push(primes[k]);
  }
}

console.log("Prime factors: " + primeFactors);

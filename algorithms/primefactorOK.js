'use strict';

function largestPrimeFactor(val, divisor = 2) {
    let square = (val) => Math.pow(val, 2);

    while ((val % divisor) != 0 && square(divisor) <= val) {
        divisor++;
    }

    return square(divisor) <= val
        ? largestPrimeFactor(val / divisor, divisor)
        : val;
}

let result = largestPrimeFactor(600851475143);

console.log(result);

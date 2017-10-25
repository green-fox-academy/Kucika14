'use strict';
// - Write a function called `sum` that sum all the numbers until the given parameter
// - The function should return the result


let num = 15;

let getSum = function(number) {
    if (number <= 1) {
        return number;
    } else {
        return getSum(number -1) + number;
    }
}

console.log(getSum(num))
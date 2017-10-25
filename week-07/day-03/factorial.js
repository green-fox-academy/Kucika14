'use strict';
// - Create a function called `factorio`
//   that returns it's input's factorial

let num = 4;

let factorio = function(number) {
    if (number <= 1) {
        return number;
    } else {
        return factorio(number -1) * number;
    }
}
console.log(factorio(num));
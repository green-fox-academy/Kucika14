
'use strict';
// - Create a variable named `abc` with the following content: `["Arthur", "Boe", "Chloe"]`
// - Swap the first and the third element of `abc`

let abc = ['Arthur', 'Boe', 'Chloe'];

let swapper = function(array) {
    [array[0], array[2]] = [array[2], array[0]];
    return array;
}

console.log(swapper(abc));
        
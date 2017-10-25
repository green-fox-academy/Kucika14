'use strict';
// - Create (dynamically*) a two dimensional list
//   with the following matrix**. Use a loop!
//
//   0 0 0 1
//   0 0 1 0
//   0 1 0 0
//   1 0 0 0
//
// - Print this two dimensional list to the console
//
// * size should depend on a variable
// ** Relax, a matrix is just like an array


let matrix = [];
let matrixSize = 3
for (let i = 0; i < matrixSize; i++) {
    let box = [];
    for (let j = 0; j < matrixSize; j++) {
        if (i === j) {
            box.push(1)
        } else {
            box.push(0)
        }
    }
    matrix.push(box);
    console.log(matrix[i])
}

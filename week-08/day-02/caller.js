'use strict';

// Implement the selectLastEvenNumber function that takes an array and callback,
// it should call the callback immediately with the last even number on the array


function printNumber(num) {
  console.log(num);
}



let selectLastEvenNumber = function(array, callback) {
    let numList = array.filter(function(num) {
        return num % 2 === 0;
    })
    callback(numList[numList.length-1]);
}

selectLastEvenNumber([2, 5, 7, 8, 9, 11], printNumber); // should print 8
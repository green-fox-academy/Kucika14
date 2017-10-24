'use strict';

// Write a program that stores 3 sides of a cuboid as variables (floats)
// The program should write the surface area and volume of the cuboid like:
//
// Surface Area: 600
// Volume: 1000

let a = 3.5;
let b = 4.5;
let c = 5.5;

console.log('volume '+ (a*b*c));
console.log('surface ' + 2*(a*b+a*c+b*c));
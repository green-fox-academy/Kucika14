'use stirct';

var test = require('tape');
var summa = require('./sum.js');

const sumy = new summa();

test('10', function(t) {
    t.equal(sumy.sum([5,5]), 10);
    t.end();
})

test('add three num', function(t) {
    t.equal(sumy.sum([2,5,8]), 15);
    t.end();
})

test('no numbers', function(t) {
    let ayy = sumy.sum(['kecske', 'malac', 'csirke'])
    t.error(ayy);
    t.end();


})
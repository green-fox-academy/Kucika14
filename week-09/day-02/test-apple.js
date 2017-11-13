'use strict';

var test = require('tape')
var appleTree = require('./apple.js')

test('print apple', function(t) {
    t.equal(appleTree(), 'apple');
    t.end();
})
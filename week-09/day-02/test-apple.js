'use strict';

var test = require('tape');
var getApple = require('./apple.js')

test('print apple', function(t) {
    t.equal(getApple(), 'apple');
    t.end();
})
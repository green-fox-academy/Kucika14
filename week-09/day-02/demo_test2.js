'use strict';

let test = require('tape')
let whoIsStrugglingNow = require('./demo');

test('who is struggling right now', function(t){
    t.equal(whoIsStrugglingNow('me'), 'me')
    t.end()
})
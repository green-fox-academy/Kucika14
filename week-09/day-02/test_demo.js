'use strict';

let test = require('tape')
let whoIsStrugglingNow = require('./demo.js')


test('who struggling', function(t) {
    t.equal(whoIsStrugglingNow('me'), 'me')
    t.end()
})


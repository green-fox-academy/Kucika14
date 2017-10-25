'use strict';
// - Create variable named `al` and assign the value `Greenfox` to it
// - Create a function called `greet` that greets it's input parameter
//     - Greeting is printing e.g. `Greetings, dear Greenfox`
//     - Prepare for the special case when no parameters are given
// - Greet `al`



let al = 0;

let greet = function(name) {
    if (name) {
        console.log('Greetings dear ' + name)
    } else {
        console.log('who are you?')
    }
}

greet(al);
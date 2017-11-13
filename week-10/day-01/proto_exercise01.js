'use strict';

// Create a constructor for creating Animals.
// it should take one parameter: what the animal says
// Every animal should have a method called say() that prints what the animal says

const Animal = function(voice) {
    this.voice = voice
}

Animal.prototype.say = function() {
    console.log(this.voice)
}

const cat = new Animal('meow')
const dog = new Animal('woof')

cat.say()
dog.say()
function Animal() {
    this.hunger = 5;
    this.thrist = 5;
    this.eat = function() {
        this.hunger -= 1;
    }
    this.drink = function() {
        this.thrist -= 1;
    }
    this.play = function() {
        this.hunger += 1;
        this.thrist += 1;
    }
}


function Farm() {
    this.slots = slots;
    this.animal = [];
    for (let i = 0; i < slots; i++) {
        this.animal.push(new  Animal());
    }
    this.breed = function() {
        if
    }
}
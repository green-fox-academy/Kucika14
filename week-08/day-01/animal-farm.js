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


function Farm(slots) {
    this.slots = slots;
    this.animal = [];
    for (let i = 0; i < slots; i++) {
        this.animal.push(new  Animal());
    }
    this.breed = function() {
        if (this.animal.length < this.slots) {
            this.animal.push(new  Animal());
        }
    }
    this.slaughter = function() {

    }
    this.progress = function() {
        this.animal.forEach(function(e){
            let randomList = [];
            let randomNumber = Math.random();
            for (let i = 0; i < 3; i++) {
                randomList.push(randomList);
            }
            if (randomList[0] > 0.5) {
                Animal.eat();
            } else if ( randomList[1] > 0.5) {
                Animal.drink();
            } else (randomList[2] > 0.5) {
                Animal.play();
            }
        })
    }
}

let farm = Farm(20)

farm.breed
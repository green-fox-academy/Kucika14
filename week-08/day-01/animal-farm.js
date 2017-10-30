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
    this.animals = [];
    for (let i = 0; i < slots; i++) {
        this.animals.push(new  Animal());
    }
    this.breed = function() {
        if (this.animals.length < this.slots) {
            this.animals.push(new  Animal());
        }
    }
    this.slaughter = function() {
        let listOfHunger = [];
        this.animals.forEach(function(e) {
            listOfHunger.push(e.hunger);
        })
        let leastHungry = Math.min.apply(Math, listOfHunger);
        this.animals.splice(listOfHunger.indexOf(leastHungry),1);


    }
    this.progress = function() {
        this.animals.forEach(function(e){
            let randomList = [];
            for (let i = 0; i < 3; i++) {
                let randomNumber = Math.random();
                randomList.push(randomNumber);
            }
            if (randomList[0] > 0.5) {
                e.eat();
            }
            if ( randomList[1] > 0.5) {
                e.drink();
            }
            if (randomList[2] > 0.5) {
                e.play();
            }
        })
    }
}

let myFarm = new Farm(20)

myFarm.breed()
myFarm.progress()
myFarm.progress()
myFarm.progress()
myFarm.progress()
myFarm.progress()
myFarm.slaughter()

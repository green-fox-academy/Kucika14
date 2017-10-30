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
        this.hunger -= 1;
        this.thrist -= 1;
    }
}
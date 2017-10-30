function Sharpie() {
    this.color = 'red',
    this.width = 10,
    this.inkAmount = 100;
    this.useSharpie = function()  {
        this.inkAmount -= this.width;
    }
}
let reddy = new Sharpie();
while (reddy.inkAmount > 0) {
    reddy.useSharpie();
    console.log(reddy.inkAmount)
}

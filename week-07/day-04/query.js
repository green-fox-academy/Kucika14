'use stirct'

let king = document.getElementById('b325');
console.log('king', king)

let conceited = document.getElementsByClassName('b326');
alert(conceited);

let businessLamp = document.getElementsByClassName('big')
console.log('big', businessLamp);

let conceitedKing = document.querySelectorAll('.container div');
conceitedKing.forEach(function(e) {
    alert(e);
});

let noBusiness = document.querySelectorAll('div');
noBusiness.forEach(function(e) {
    console.log(e);
});

let allBizniss = document.querySelectorAll('p');
alert(allBizniss);
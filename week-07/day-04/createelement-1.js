let greenFox = document.createElement('li');
greenFox.textContent = 'The Green Fox';

let lamplighter = document.createElement('li');
lamplighter.textContent = 'The Lamplighter';

let adder = document.querySelector('ul');
adder.appendChild(greenFox);
adder.appendChild(lamplighter);

let heading = document.createElement('h1');
heading.textContent = 'I can add elements to the DOM!';

let headAdder = document.querySelector('.container');
headAdder.appendChild(heading);
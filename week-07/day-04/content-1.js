let head = document.querySelector('h1');
alert(head.textContent);

let firstPar = document.querySelectorAll('p');
console.log(firstPar[0].textContent);

let kecske = document.querySelectorAll('p');
alert(kecske[1].textContent);

head.textContent = 'New Content'

firstPar[2].textContent = firstPar[0].textContent;
let image = document.querySelector('img');
image.setAttribute('src', 'https://memegenerator.hu/uploads/images/Cvp2SvCAL.jpg');

let link = document.querySelector('a');
link.setAttribute('href', 'https://www.greenfoxacademy.com/')

let buttonDisable = document.querySelectorAll('button');
buttonDisable[1].disabled = true;
buttonDisable[1].textContent = 'Don\'t click me!'
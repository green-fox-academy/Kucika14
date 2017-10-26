let listOfWords = ['apple', 'banana', 'cat', 'dog'];

let replace = document.querySelectorAll('li');
replace.forEach(function(e, i) {
    e.textContent = listOfWords[i];
})


let background = document.querySelector('ul');
background.style.background = 'limegreen';
background.style.borderRadius = '35px';
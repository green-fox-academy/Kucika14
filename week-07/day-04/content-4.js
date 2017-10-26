let listOfWords = ['apple', 'banana', 'cat', 'dog'];

let replace = document.querySelectorAll('li');
replace.forEach(function(e, i) {
    e.textContent = listOfWords[i];
})

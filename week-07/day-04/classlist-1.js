let pTags = document.querySelectorAll('p');
if (pTags[2].classList.contains('red-dot')) {
    alert('OMG DOTS!')
};

if (pTags[3].textContent === 'dolphin' ) {
    pTags[0].textContent = 'pear'
};

if (pTags[0].classList.contains('apple')) {
    pTags[2].textContent = 'dog'
}

pTags[0].classList.add('red');
pTags[1].style.borderRadius = '0px';
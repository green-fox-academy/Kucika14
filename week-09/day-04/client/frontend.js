'use strict'

const body = document.querySelector('body')
let bookstore = new XMLHttpRequest();

let ajax = function(method, data, response, callback) {
    data = data ? data : null;
    bookstore.open(method, 'http://localhost:8080' + response);
    bookstore.setRequestHeader('Content-Type', 'application/json');
    bookstore.send(JSON.stringify(data));
    bookstore.onreadystatechange = function() {
        if (bookstore.readyState === XMLHttpRequest.DONE) {
            callback( JSON.parse(bookstore.response))
        }
    };
};

let doRequest = function(){
    ajax('GET', '', '/data', handleData);
} 


function handleData(data) {
    console.log(data)
    data.forEach(function(e) {
        let bookTitle = document.createElement('h1');
        body.appendChild(bookTitle);
        bookTitle.textContent = e.book_name;
        let autName = document.createElement('p');
        body.appendChild(autName);
        autName.textContent = e.aut_name;
        let categrory = document.createElement('p');
        body.appendChild(categrory);
        categrory.textContent = e.cate_descrip;
        let publisherName = document.createElement('p');
        body.appendChild(publisherName);
        publisherName.textContent = e.pub_name;
        let price = document.createElement('p');
        body.appendChild(price);
        price.textContent = e.book_price +'$';
        
    })
}

doRequest()
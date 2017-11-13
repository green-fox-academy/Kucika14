'use strict';

let ul = document.querySelector('ul')
        
let doRequest = function(callback) {
    var x = new XMLHttpRequest();
    x.open('GET', 'http://secure-reddit.herokuapp.com/simple/posts');
    x.onload = function() {
        callback(x.responseText)
    };
    x.send(null);
}



function handleData(data){
    let wholeReddit = JSON.parse(data);
    let reddit = wholeReddit.posts;
    console.log(reddit) 
    reddit.forEach(function(e) {
        let link = document.createElement('a');
        ul.appendChild(link);
        link.setAttribute('href', e.url);
        link.textContent = e.title;
        

    })
    
}


doRequest(handleData)


let postOnReddit = function()
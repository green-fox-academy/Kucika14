'use strict';

let music = document.querySelector('.playlists')
let foxPlayer = new XMLHttpRequest();

let ajax = function(method, data, response, callback) {
    data = data ? data : null;
    foxPlayer.open(method, 'http://localhost:8080' + response);
    foxPlayer.setRequestHeader('Content-Type', 'application/json');
    foxPlayer.send(JSON.stringify(data));
    foxPlayer.onreadystatechange = function() {
        if (foxPlayer.readyState === XMLHttpRequest.DONE) {
            callback( JSON.parse(foxPlayer.response))
        };
    };
};

let playLists = function(){
    ajax('GET', '', '/playlists', handleData);
} 

let handleData = (data) => {
    console.log(data)
    data.forEach(function(e) {
        let track = document.createElement('p');
        music.appendChild(track);
        track.textContent = e.title;
    })
}


playLists()

'use strict';

let playTrack = document.querySelector('.playlists')
let trackList = document.querySelector('.tracklist')


let ajax = function(method, data, response, callback) {
    let foxPlayer = new XMLHttpRequest();
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
    ajax('GET', '', '/playlists', playListData);
}

let playListData = (data) => {
    console.log(data)
    data.forEach(function(e) {
        let play = document.createElement('p');
        playTrack.appendChild(play);
        play.textContent = e.title;
    })
}

let trackInfo = function(){
    ajax('GET', '', '/trackinfo', trackInfoData);
}

let trackInfoData = (data) => {
    data.forEach(function(e) {
        let track = document.createElement('p');
        trackList.appendChild(track);
        track.textContent = e.id;
        track.textContent += ". " + e.title;
    })
}



playLists()
trackInfo()

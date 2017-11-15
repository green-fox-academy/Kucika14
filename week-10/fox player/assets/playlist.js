'use strict';

let playTrack = document.querySelector('.playlists')

let listPlayLists = function(){
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

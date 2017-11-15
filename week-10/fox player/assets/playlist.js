'use strict';

let playTrack = document.querySelector('.playlists')

let listPlayLists = function(){
    ajax('GET', '', '/playlists', playListData);
}

let playListData = (data) => {
    console.log(data)
    data.forEach(function(e) {
        let play = document.createElement('li');
        playTrack.appendChild(play);
        play.textContent = e.title;
    })
    highLight()

}


let highLight = () => {
    let liElements = playTrack.querySelectorAll('li')
    liElements.forEach(function(e){
        e.addEventListener('click', function() {
            liElements.forEach(e => e.classList.remove('active'))
            e.classList.add('active');
        })
    })
}


let create = () => {
    let addPlayList = document.querySelector('.plus')
    let body = document.querySelector('body')
    addPlayList.addEventListener('click' , function() {
        let div = document.createElement('div')
        div.classList.add('userbox')
        body.appendChild(div)
        let inputElement = `<input type="text" placeholder="kecskeeeeeee!!!!!!!!">
                            <button class="ok"></button>
                            <button class="cancel"></button>`
        div.innerHTML = inputElement;
    })
}

let postList = function() {
    ajax('POST', {'szia': 'hali'}, '/trackinfo', console.log)
}

create()


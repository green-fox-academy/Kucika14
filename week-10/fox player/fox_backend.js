'use strict';

const express = require('express');
const app = express()

app.use('/', express.static('./assets'));
app.use(express.json())


app.get('/', function(request, response) {
  response.sendFile(__dirname + '/fox_player.html');
});

app.get('/playlists', function(request, response) {
    let playLists = [
        { "id": 1, "title": "Favorites", "system": 1},
        { "id": 2, "title": "Music for programming", "system": 0},
        { "id": 3, "title": "Driving", "system": 0},
        { "id": 5, "title": "Fox house", "system": 0},
    ]
    response.json(playLists)
})

app.get('/trackinfo', function(request, response) {
    let trackList = [
        { "id": 1, "title": "birkát cserélek búzáért", "system": 1},
        { "id": 2, "title": "három az egyben váltok követ bármire", "system": 0},
        { "id": 3, "title": "Driving", "system": 0},
        { "id": 5, "title": "Fox house", "system": 0},
    ]
    response.json(trackList)
})

app.post('/trackinfo', function(request, response) {
    console.log(request.body)
    response.json({'status': 'done'})
})



app.listen(8080, () => console.log('server running'));

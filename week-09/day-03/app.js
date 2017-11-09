'use strict';

const express = require('express');
const app = express()

express.json.type = 'application/json'
app.use('/assets', express.static('./assets'));
app.use(express.json())

app.get('/', function(request, response) {
    response.sendFile(__dirname + '/index.html');
})


app.get('/doubling', function(request, response) {
    if (request.query.input === undefined) {
        response.json({ 'error' : 'Please provide a number!'})
    } else {
        response.json({
            'received': request.query.input,
            'result': request.query.input * 2
        })
    }
})

app.get('/greeter', function(request, response) {
    if (request.query.name === undefined) {
        response.json({
            'error': 'Please provide a name!'
        })
    } else if (request.query.title === undefined) {
            response.json({
                'error': 'Please provide a title!'
            })
    } else {
        response.json({
            'welcome_message': 'Oh, hi there ' + request.query.name +', my dear ' + request.query.title + '!'
        })
    }
})


app.get('/appenda/:appendable', function(request, response) {
    response.json({
        'appended' : request.params.appendable + 'a'
    })
})

app.post('/dountil/:what', function(request, response) {
    let result = 0
    if (request.body.until === undefined) {
        response.json({
            'error' : 'Please provide number'
        })
    } else {
        if (request.params.what === 'sum') {
            result = sum(request.body.until)
        } else if (request.params.what === 'factor') {
            result = factor(request.body.until)
        }
        response.json({
            'result' : result
        })
    }
})

app.listen(8080);


let sum = function(x) {
    let sum = 0
    for (let i = 0; i <= x; i++) {
        sum += i
    }
    return sum;
}


let factor = function(x) {
    let factor = 1
    for (let i = 1; i <= x; i++) {
        factor *= i
    }
    return factor;
}



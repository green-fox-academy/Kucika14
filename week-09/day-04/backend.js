'use strict';


const express = require('express');
const app = express()
const mysql = require('mysql');

app.use('/client', express.static('./client'));
app.use(express.json())



const connection = mysql.createConnection({
  host     : 'localhost',
  user     : 'root',
  password : '2312paska',
  database : 'bookstore'
});
 
connection.connect();


app.get('/', function(request, response) {
  response.sendFile(__dirname + '/index.html');
});

let getDatabase = function(tableName, what, callback) {
  let searchQuery = 'SELECT' + what + 'FROM' + tableName;
  connection.query(searchQuery, function(error, results, fields) {
    callback(results, what)
  })
}

let handleSqlData = function(sqlResults, fieldName) {
  let returnData = []
  sqlResults.forEach(function(e) {
    returnData.push(element[fieldName])
  })
}

app.get('/data', function(request, response) {
  let data = []
  connection.query('select book_name from book_mast;', function(error, response, fields) {
    data = results.map(function(element) {
      response.send(data)
    })
  })
}
   
app.listen(8080);
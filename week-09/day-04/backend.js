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

app.get('/data', function(request, response) {
    connection.query(`SELECT book_name, aut_name, cate_descrip, pub_name, book_price FROM book_mast
                      JOIN author ON author.aut_id = book_mast.aut_id
                      JOIN category ON category.cate_id = book_mast.cate_id
                      JOIN publisher ON publisher.pub_id = book_mast.pub_id`, function (error, results) {
      if (error) throw error;
      response.send(results);
  });
});


app.listen(8080);
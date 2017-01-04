// MySQL in Express.js
'use strict';

var express = require('express');
var mysql = require('mysql');
var app = express();

var connection = mysql.createConnection({
  host     : 'localhost',
  user     : 'root',
  password : '',
  database : 'test'
});

connection.connect();

app.get('/', function(req, res) {
  connection.query('SELECT * FROM house', function(err, rows, fields) {
    if (err) throw err;
    console.log(rows);
  });
});

app.listen(3000, function() {
  console.log('Server is up and running on port: 3000');
});

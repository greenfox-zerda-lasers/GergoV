'use strict';

var express = require('express');
var mysql = require('mysql');
var app = express();

var connection = mysql.createConnection({
  host     : 'localhost',
  user     : 'root',
  password : '',
  database : 'foxplayer'
});
connection.connect();
 
app.get('/', function(req, res) {
	connection.query('SELECT * FROM house', function(err, rows, fields) {
		if (err) throw err;
  		res.send(rows);
	});
});

app.get('/create', function(req, res) {
	connection.query({
		sql: 'INSERT INTO playlists(playlist, protected) VALUES(?, ?)',
		values: ['Hello', 0]
	}, function(err, rows, fields) {
		if (err) throw err;
  		res.send(rows);
	});
});

app.listen(3000, function(){
	console.log('SERVER IS UP AND RUNNIN on port: 3000')
});

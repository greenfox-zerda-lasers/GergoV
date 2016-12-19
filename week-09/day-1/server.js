'use strict';

var http = require('http');
var date = new Date();

var server = http.createServer(function cica(req, res) {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end('Hey! How are you? The current date is: ' + date);
});

server.listen(3000, '127.0.0.1');

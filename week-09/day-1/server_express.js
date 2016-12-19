'use strict';

var express = require('express');

var app = express();
var date = new Date();

app.get('*', function (req, res) {
  res.send('You made a request of type: ' + req.method + ' at ' + date + ' to access path ' + req.url + '.');
});

app.listen(3000);

'use strict';

const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');

// Express config
const app = express();
const portNum = 8080;
app.use(bodyParser.json());

app.use(express.static('app'));

// Endpoints
app.get('/files', function(req, res) {
  res.send('You have requested file list.');
});

console.log('Server up on port ' + portNum + '.');
app.listen(portNum);

/* eslint-env node */

'use strict';

const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');
const path = require('path');
const p = './_data/';

// Express config
const app = express();
const portNum = 8080;
app.use(bodyParser.json());

app.use(express.static('app'));
app.use(express.static('_data'));

// Endpoints
app.get('/files', function(req, res) {

  let imageList = [];

  // Parse files from path
  fs.readdir(p, function (err, files) {
    if (err) {
      throw err;
    }

    files.map(function addPath(file) {
      return path.join(p, file); // Add path to filenames
    }).filter(function filterFiles(file) {
      return fs.statSync(file).isFile(); // Return files only
    }).forEach(function compileArray(file) {
      imageList.push(file); // Compile list of files in array
    });

    res.send(imageList);
  });
});

console.log('Server up on port ' + portNum + '.');
app.listen(portNum);

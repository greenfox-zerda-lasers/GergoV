/* eslint-env node */

'use strict';

const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');
const path = require('path');
const imageMeta = require('./_data/data.json');

// Express config
const app = express();
const portNum = 8080;
app.use(bodyParser.json());

app.use(express.static(__dirname + '/app'));
app.use('/_data', express.static(__dirname + '/_data'));

// Gallery image related data
const p = './_data/';
console.log(imageMeta[0].title);
// Endpoints
app.get('/files', function(req, res) {

  let imageList = [];

  // Parse files from path
  fs.readdir(p, function (err, files) {
    if (err) {
      throw err;
    }

    let imageBatch = files.map(function addPath(file) {
      return path.join(p, file); // Add path to filenames
    }).filter(function filterFiles(file) {
      return fs.statSync(file).isFile(); // Return files only
    })

    imageBatch.forEach(function compileArray(file, index) {
      console.log(file, index);
      imageList.push({ "url":file, "title": imageMeta[index].title, "description": imageMeta[index].description }); // Compile list of files in array
    });

    res.send(imageList);
  });
});

console.log('Server up on port ' + portNum + '.');
app.listen(portNum);

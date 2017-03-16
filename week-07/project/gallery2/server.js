/* eslint-env node */

'use strict';

const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');
const path = require('path');
const ExifImage = require('exif').ExifImage;

// Express config
const app = express();
const portNum = 8080;
app.use(bodyParser.json());

app.use(express.static(__dirname + '/app'));
app.use('/_data', express.static(__dirname + '/_data'));

const p = './_data/';
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
    }).forEach(function compileArray(file, index) {
      try {
          new ExifImage({ image : file }, function (error, exifData) {
              if (error)
                  console.log('Error: '+error.message);
              else
                  console.log(exifData); // Do something with your data!
          });
      } catch (error) {
          console.log('Error: ' + error.message);
      }
      imageList.push({ "url":file, "metadata":ExifImage.exifData, }); // Compile list of files in array
    });

    res.send(imageList);
  });
});

console.log('Server up on port ' + portNum + '.');
app.listen(portNum);

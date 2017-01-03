// Server code base from GreenFox Zerda Syllabus

'use strict';

var express = require('express');
//var bodyParser = require('body-parser');

var app = express();
var playlists = [
    { "id": 21, "title": "Halahula", "artist": "Untitled artist", "duration": 545, "path": "c:/music/halahula.mp3" },
    { "id": 412, "title": "No sleep till Brooklyn", "artist": "Beastie Boys", "duration": 312.12, "path": "c:/music/beastie boys/No sleep till Brooklyn.mp3" }
]

//app.use(bodyParser.json());

app.get('/playlists', function (req, res) {
  res.json(playlists);
});

app.get('/teapot', function (req, res) {
  res.sendStatus(418);
});

module.exports = app;

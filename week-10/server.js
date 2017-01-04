// FoxPlayer Node.JS server

'use strict';

var express = require('express');
//var bodyParser = require('body-parser');

var app = express();
// default playlists request response: all tracks
var playlists = [
    { "id": 21, "title": "Halahula", "artist": "Untitled artist", "duration": 545, "path": "c:/music/halahula.mp3" },
    { "id": 412, "title": "No sleep till Brooklyn", "artist": "Beastie Boys", "duration": 312.12, "path": "c:/music/beastie boys/No sleep till Brooklyn.mp3" }
]

//app.use(bodyParser.json());

// PLAYLISTS
app.get('/playlists', function (req, res) {
  res.json(playlists);
});

app.post('/playlists', function (req, res) {
  // req: playlist name
  // return: full list/only new
  res.json(playlists);
});

app.delete('/playlists/:id', function (req, res) {
  // req: playlist id
  // ! Can't delete system playlist
  // ERR: if id missing or not enum., error in JSON (why?)
});

// PLAYLIST tracks
app.get('/playlist-tracks/', function (req, res) {
  // no id: all tracks in root folder
  // list playlist tracks
});

app.get('/playlist-tracks/:playlist_id', function (req, res) {
  // list all trakcs in playlist
});

app.post('/playlist-tracks/:playlist_id', function (req, res) {
  // add track to playlist
});

app.delete('/playlist-tracks/:playlist_id/:track_id', function (req, res) {
  // list all trakcs in playlist
  // missing or not enumerable id: JSON error
});


module.exports = app;

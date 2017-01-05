// FoxPlayer Node.JS server

// Plan:
// Database init: parse files, update DB
// Express server: Endpoints
// Request handler: Database functions, modifying data and setting return values

'use strict';

var express = require('express');
var bodyParser = require('body-parser');

var app = express();

app.use(bodyParser.json());

// DB mock
var tracks = [
    { "id": 21, "title": "Halahula", "artist": "Untitled artist", "duration": 545, "path": "c:/music/halahula.mp3" },
    { "id": 412, "title": "No sleep till Brooklyn", "artist": "Beastie Boys", "duration": 312.12, "path": "c:/music/beastie boys/No sleep till Brooklyn.mp3" }
];
var playlists = [
  { "playlist_id": 0, "name": "Favorites", "tracks": [] },
  { "playlist_id": 1, "name": "Music for coding", "tracks":[21, 412]},
  { "playlist_id": 2, "name": "RAVE", "tracks":[21, 412]},
  { "playlist_id": 3, "name": "Music for driving", "tracks":[21, 412]},
  { "playlist_id": 4, "name": "ROCK", "tracks":[]},
  { "playlist_id": 5, "name": "Bowie", "tracks":[]},
];


// *** Endpoints ***

// PLAYLISTS

// List all the playlists
app.get('/playlists', function listAllTracks(req, res) {
  res.json(playlists);
});

// Create playlist
app.post('/playlists', function (req, res) {
  var playlistName = req.body.playlist;
  // NOTE: Mocked version, no DB, accepts app/JSON post
  // NOTE: Must create unique playlist id!!!
  playlists.push({
      "playlist_id": playlists.length,
      "name": playlistName,
      "tracks": []
  });

  res.json(playlists);
});

// Delete playslist
app.delete('/playlists/:id', function(req, res) {
  var playlistToDelete = req.params.id;

  // Final function comes here:
  var deletePlaylist = function(playlistToDelete) {
    console.log('Playlist with ID ' + playlistToDelete + ' is to be deleted!');
  };
  deletePlaylist(playlistToDelete);

  res.json(playlists);
  // req: playlist id
  // ! Can't delete system playlist
  // ERR: if id missing or not enum., error in JSON (why?)
});

// PLAYLIST tracks
// List all tracks
app.get('/playlist-tracks/', function(req, res) {
  // no id: all tracks in root folder
  // list playlist tracks
});

// List playlist tracks
app.get('/playlist-tracks/:playlist_id', function(req, res) {
  // list all trakcs in playlist
});

// Add track to playlist
app.post('/playlist-tracks/:playlist_id', function(req, res) {
  // add track to playlist
});

// Delete track from playlist
app.delete('/playlist-tracks/:playlist_id/:track_id', function (req, res) {
  // list all trakcs in playlist
  // missing or not enumerable id: JSON error
});


app.listen(3000, function logServerStatus() {
  console.log('FoxPlayer server up and running on localhost:3000');
});

// GreenFox Syllabus - test.js

'use strict';

var test = require('tape');
var request = require('supertest');
var app = require('./server.js');

test('Testing FoxPlayer backend, YO!', function (t) {
  t.end();
});

// GET playlists
test('Playlists returned', function (t) {
  request(app)
    .get('/playlists')
    .expect('Content-Type', /json/)
    .expect(200)
    .end(function (err, res) {
      t.error(err, 'No error');
      t.end();
    });
});

test('Playlist format is proper', function (t) {
  request(app)
    .get('/playlists')
    .expect('Content-Type', /json/)
    .expect(200)
    .expect(function(res) {
      Number.isInteger(res.body.id) 
    })

    .end(function (err, res) {
      t.error(err, 'No error');
      t.end();
    });
});

// POST playlists
/*
Creates a new playlist
Required field is only a "playlist" property that contains the name of the playlist
System playlist cannot be created by the client
Return playlists in the order they were adde
*/
test('New playlist created', function(t) {
  request(app)
    .post('/playlists')
    .expect(200)
    .end(function (err, res) {
      t.error(err, 'No error');
      t.end();
    });
});

// DELETE playlists/:id
// GET /playlist-tracks
// GET /playlis-tracks/:playlist_id

// DELETE /playlist-tracks/:playlist_id/:track_id

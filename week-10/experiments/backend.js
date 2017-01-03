// FoxPlayer backend service

'use strict';

var express = require('express');
var test = require('tape');
var request = require('supertest');

var app = express();


app.get('/valami', function (req, res) {
  res.send( 'lefutottam ej' );
});

test('GET /valami', function (assert) {
  request(app)
  .get('/valami')
  .expect(200)
});

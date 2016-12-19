'use strict';

var express = require('express');

var myDB = require('./todo.json');

var app = express();

app.get('/todos', function listAllTodos(req, res) {
  res.send(myDB);
});

app.get('/todos/:id', function listAllTodos(req, res) {
  var id = req.params.id;
  res.send(myDB[id]);
});


app.listen(3000);

// Todo app node.js server

'use strict';

var express = require('express');
var bodyParser = require('body-parser');
var sql = require('./requests.js');

var app = express();

var jsonParser = bodyParser.json();
var urlencodedParser = bodyParser.urlencoded({ extended: true });

// Handled HTTP requests

app.get('/todos', function listAllTodos(req, res) {
  var todoList = sql.listTodos();
  res.send();
});

/*
app.get('/todos/:id', function listAllTodos(req, res) {
  var id = req.params.id;
  res.send(myDB[id]);
});

app.use(bodyParser.json());
app.post('/todos/add/', urlencodedParser, function addTodo(req, res) {
  console.log(req.body);
  var entry = {
    completed: Boolean(req.body.completed),
    id: myDB.length + 1,
    text: req.body.text,
  };
  myDB.push(entry);
  res.send(JSON.stringify(entry));
});
*/

app.listen(3000);

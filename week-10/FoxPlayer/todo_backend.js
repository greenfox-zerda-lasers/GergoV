// Todo app node.js server - Universal

'use strict';

var express = require('express');
var bodyParser = require('body-parser'); // for JSON?
var myDB = require('../../week-09/day-1/todo.json'); // NOTE: Testing DB

var app = express();

var jsonParser = bodyParser.json();
var urlencodedParser = bodyParser.urlencoded({ extended: true });

// 1. List todos
app.get('/todos/', function listAllTodos(req, res) {
  res.send(myDB);
});

// 2. Get a single todo item
app.get('/todos/:id', function listAllTodos(req, res) {
  var id = req.params.id;
  res.send(myDB[id]);
});

// 3. Add todo
// NOTE: curl localhost:3000/todos/add/ -d '{"text": "Buy eggs"}' -H 'Content-Type: application/json'

app.use(jsonParser); // Use body parser NOTE: What does it in fact do?
app.post('/todos/add', urlencodedParser, function addTodo(req, res) {
  console.log(req.body);
  var entry = {
    completed: Boolean(req.body.completed),
    id: myDB.length + 1,
    text: req.body.text,
  };
  myDB.push(entry);
  res.send(JSON.stringify(entry));
});

// 4. Complete todo
app.put('/todos/complete/:id', function (req, res) {
  var id = req.params.id;
  /*
  myDB[id].completed = !myDB[id].completed;
  res.send('Task ' + id + ' ' + req.body + ' ' + myDB[id].completed);
  */
  res.send('Put request at ' + myDB[id]);
});

// 5. Delete todo
app.delete('/todos/delete/', function (req, res) {
  res.send('Got a DELETE request at /user')
});

app.listen(3000);

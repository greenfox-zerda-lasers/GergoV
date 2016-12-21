// MySQL Todo Manager

var mysql = require('mysql');

var con = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'm2st3r',
    database: 'todoapp'
});

function connectToDB () {
  con.connect(function(err){
    if(err){
      console.log('Error connecting to Db');
      return;
    }
    console.log('Connection established');
  });
};

function endConnection() {
  con.end(function(err) {
    // Terminate connection gracefully.
  });
};

// Todo functions:
var listTodos = function() {
    con.query('SELECT * FROM todos', function(err, rows){
        if(err) {
          throw err;
        } else {
          return rows;
        }
    });
};

function createTodo(text) {
    con.query('INSERT INTO todos (text) VALUES (?)', text, function (err, res){
        if(err) throw err;

        console.log('Last insert IDE:', res.insertId);
    });
};

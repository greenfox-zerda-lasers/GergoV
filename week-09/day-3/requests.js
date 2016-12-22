// MySQL Todo Manager

var mysql = require('mysql');

var con = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'm2st3r',
    database: 'todoapp'
});

module.exports.connectToDB = function () {
  con.connect(function(err){
    if(err){
      console.log('Error connecting to Db');
      return;
    }
    console.log('Connection established');
  });
};

module.exports.endConnection = function () {
  con.end(function(err) {
    // Terminate connection gracefully.
  });
};

// Todo functions:
module.exports.listTodos = function() {
    con.query('SELECT * FROM todos', function(err, rows){
        if(err) {
          throw err;
        } else {
          return rows;
        }
    });
};

module.exports.createTodo = function (text) {
    con.query('INSERT INTO todos (text) VALUES (?)', text, function (err, res){
        if(err) throw err;

        console.log('Last insert IDE:', res.insertId);
    });
};

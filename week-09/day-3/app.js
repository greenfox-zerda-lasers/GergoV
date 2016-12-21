// MySQL Todo Manager

var mysql = require('mysql');

var con = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'm2st3r',
    database: 'todoapp'
});

con.connect(function(err){
    if(err){
        console.log('Error connecting to Db');
        return;
    }
    console.log('Connection established');
});

//listTodos();
createTodo('Test node functions');

con.end(function(err) {
    // Terminate connection gracefully.
});

// Todo functions:

function listTodos() {
    con.query('SELECT * FROM todos', function(err, rows){
        if(err) throw err;

        console.log('List of todos:\n');
        console.log(rows);
    });
};

function createTodo(text) {
    con.query('INSERT INTO todos (text) VALUES (?)', text, function (err, res){
        if(err) throw err;

        console.log('Last insert IDE:', res.insertId);
    });
};
